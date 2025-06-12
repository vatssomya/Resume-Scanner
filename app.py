from flask import Flask, render_template, request
import joblib
import re
import docx
import PyPDF2

app = Flask(__name__)

svc_model = joblib.load("clf.sav")
tfidf = joblib.load("tfidf.sav")
le = joblib.load("encoder.sav")


def cleanResume(txt):
    cleanText = re.sub(r'http\S+\s', ' ', txt)
    cleanText = re.sub(r'RT|cc', ' ', cleanText)
    cleanText = re.sub(r'#\S+\s', ' ', cleanText)
    cleanText = re.sub(r'@\S+', '  ', cleanText)
    cleanText = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub(r'\s+', ' ', cleanText)
    return cleanText


def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text


def extract_text_from_txt(file):
    try:
        text = file.read().decode('utf-8')
    except UnicodeDecodeError:
        text = file.read().decode('latin-1')
    return text


def handle_file_upload(file_storage):
    filename = file_storage.filename
    extension = filename.split('.')[-1].lower()
    if extension == 'pdf':
        return extract_text_from_pdf(file_storage)
    elif extension == 'docx':
        return extract_text_from_docx(file_storage)
    elif extension == 'txt':
        return extract_text_from_txt(file_storage)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")


def predict_category(resume_text):
    cleaned_text = cleanResume(resume_text)
    vectorized_text = tfidf.transform([cleaned_text]).toarray()
    predicted = svc_model.predict(vectorized_text)
    category = le.inverse_transform(predicted)
    return category[0]


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    extracted_text = None
    error = None

    if request.method == 'POST':
        file = request.files.get('resume')
        if file:
            try:
                extracted_text = handle_file_upload(file)
                result = predict_category(extracted_text)
            except Exception as e:
                error = str(e)

    return render_template('index.html', result=result, extracted_text=extracted_text, error=error)


if __name__ == '__main__':
    app.run(debug=True)
