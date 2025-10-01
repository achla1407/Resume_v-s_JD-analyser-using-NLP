import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text

def get_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(similarity[0][0] * 100, 2)

def extract_keywords(text, n=15):
    vectorizer = TfidfVectorizer(stop_words="english", max_features=n)
    vectorizer.fit([text])
    return vectorizer.get_feature_names_out()
#STREAMLIT APP
st.set_page_config(page_title="Resume Matcher", page_icon="📄", layout="centered")

st.title(" Resume vs Job Description Matcher")
st.write("Upload your resume and paste a job description to see how well they match!")

jd_text = st.text_area("Paste Job Description here:", height=200)
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if st.button("Analyze"):
    if not jd_text:
        st.warning("⚠️ Please paste a job description!")
    elif not resume_file:
        st.warning("⚠️ Please upload your resume (PDF)!")
    else:
        resume_text = extract_text_from_pdf(resume_file)

        if not resume_text.strip():
            st.error("Could not extract text from the resume. Please upload a text-based PDF.")
        else:
            score = get_similarity(resume_text, jd_text)

            st.subheader("Match Result")
            st.metric("Overall Match Score", f"{score}%")
            st.progress(int(score))

        
            jd_keywords = extract_keywords(jd_text, n=15)
            present = [kw for kw in jd_keywords if kw.lower() in resume_text.lower()]
            missing = [kw for kw in jd_keywords if kw.lower() not in resume_text.lower()]

            st.subheader("Keyword Analysis")
            st.write("✅ Present in Resume:", ", ".join(present) if present else "None")
            st.write("❌ Missing in Resume:", ", ".join(missing) if missing else "None")

            st.success("Analysis complete! ✅")
