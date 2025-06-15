# 🧠 Resume Scanner – AI-Based Role Predictor
 

## 🗂️ Overview

The **Resume Scanner** takes a `.pdf`, `.docx`, or `.txt` file, extracts the text, and compares it with predefined job role descriptions to determine the most relevant match.

This project helped build the pipeline for resume parsing, vectorization, and basic classification, which later evolved into the full RecruitGPT system.

Demo video included!
---

## 💡 Features

- Upload a **single resume**
- Extract and process resume text
- Compare with predefined job roles
- Predict the most relevant job category
- Clean and minimal frontend using Flask & Jinja

---

## 🔧 Tech Stack

| Component     | Technology Used                |
|---------------|--------------------------------|
| Language      | Python                         |
| Backend       | Flask                          |
| NLP           | TF-IDF, Cosine Similarity      |
| Resume Parsing| PyMuPDF, python-docx           |
| Frontend      | HTML, CSS (Flask templates)    |
| Data          | Sample job descriptions (custom/Kaggle) |

---

## 🛠 Functional Flow

1. **Upload resume**
2. **Extract text** based on file type
3. **Preprocess text** (lowercase, clean, remove stopwords)
4. **Match resume text** with job descriptions using TF-IDF
5. **Predict most similar role**
6. **Display prediction on web page**

---

## 🚀 Running the App Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/resume-scanner.git
cd resume-scanner

# Optional: Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

# Access in browser at:
# http://127.0.0.1:5000/
