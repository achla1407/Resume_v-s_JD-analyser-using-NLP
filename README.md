# 📄 Resume & Job Description Matcher

An intelligent web tool built with Streamlit and Scikit-learn that helps you optimize your resume for any job application. It calculates a match score and provides keyword-based feedback by comparing your resume against a job description.

### 🚀 *Live Demo:* [**https://resumev-sjd-analyser-using-nlp.streamlit.app/**](https://resumev-sjd-analyser-using-nlp.streamlit.app/)

---

### 🤔 The Problem

Manually tailoring a resume for every single job application is tedious and time-consuming. It's often difficult to know which keywords and skills to emphasize to pass through both automated Applicant Tracking Systems (ATS) and human recruiters. This tool was built to solve that problem by providing instant, data-driven feedback.



---

## ✨ Key Features

* * PDF-Format Input*: Upload your resume as a .pdf file
* * Quantitative Match Score*: Receive an overall similarity score (0-100%) that instantly tells you how well your resume aligns with the job description.
* * Keyword Analysis*:
    * *Present Keywords*: See a list of crucial keywords from the job description that are already present in your resume.
    * *Missing Keywords*: Get an actionable list of important keywords that are missing, allowing you to strategically update your resume.
* *Smart Text Processing*: Utilizes NLP techniques to clean and process text for a more accurate and meaningful comparison.
* *Interactive UI*: A clean, simple, and responsive user interface built with Streamlit, complete with a progress bar for a smooth user experience.

---

## ⚙ How It Works

The application leverages a core Natural Language Processing (NLP) pipeline to analyze the documents:

1.  *Text Extraction*: For PDF resumes, the tool uses the pdfplumber library to accurately extract all text content.
2.  *Text Cleaning & Preprocessing*: Both the resume and job description texts are standardized. This involves converting text to lowercase and removing common "stopwords" (e.g., "the," "is," "a") which don't add significant meaning.
3.  *TF-IDF Vectorization: The cleaned texts are transformed into numerical representations using the **Term Frequency-Inverse Document Frequency (TF-IDF)* algorithm from scikit-learn. TF-IDF assigns a weight to each word, signifying its importance in the context of the document. Keywords that appear frequently in the job description but not in a large corpus of general documents will receive a higher score.
4.  *Cosine Similarity: Once the resume and job description are converted into numerical vectors, **Cosine Similarity* is used to measure the cosine of the angle between them. This metric effectively determines how similar the two documents are. A score closer to 1 (or 100%) indicates a higher degree of similarity in their keyword content.

---

## 🛠 Tech Stack

* *Backend*: Python
* *Web Framework*: Streamlit
* *Machine Learning/NLP*: Scikit-learn
* *PDF Processing*: pdfplumber

