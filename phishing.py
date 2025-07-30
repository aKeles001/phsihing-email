import streamlit as st
import joblib
import time


# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")  # Save your vectorizer similarly

st.title("Phishing Email Detection")

email_text = st.text_area("Paste your email content here:")

if st.button("Predict"):
    features = vectorizer.transform([email_text])
    result = model.predict(features)[0]
    label = "✅ Ham (Safe Message)" if result == 1 else "⚠️ Spam/Phishing"
    st.write("-" * 60)
    st.write(email_text[:300] + ("..." if len(email_text) > 300 else ""))
    st.write("-" * 60)
    st.write(f"**Prediction:** {label}")
