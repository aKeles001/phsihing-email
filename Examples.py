import streamlit as st
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Email Examples for Test!")

# Define email examples with labels
email_examples = {"✈️ British Airways Compensation Email":
"""Hi John,
 
We hope this message finds you well.
 
We are pleased to inform you that a £300 British Airways travel voucher has been issued to you, which can be used on any of our future flights. This voucher has been provided following a recent flight change that did not meet our usual high standards. After a review by the Civil Aviation Authority (CAA), it was determined that the notice provided fell short of the expected minimum level.
 
To make things right, we’ve issued this voucher, which you can use for your next British Airways booking. You will find the voucher attached to this email. Alternatively, you can download it directly from your British Airways account by logging in here: https://accounts.britishairways.com/flight-credit/login
 
The voucher can be redeemed easily online or through our customer service team.
 
Thank you for your understanding, and we look forward to welcoming you on board again soon.
 
Warm regards,
The British Airways Team""",
"📅 Weekly Team Sync Reminder":
"""Hi team,

This is a reminder for our weekly team sync scheduled for Thursday at 2:00 PM.

Agenda:
- Project status updates
- Q3 planning review
- Open questions & discussion

Meeting link (Google Meet): https://meet.google.com/abc-defg-hij  
Please be ready with your updates. Let me know if you can’t attend.

Best,  
Emily Jameson  
Project Manager"""
}

# Dropdown with short labels
selected_label = st.selectbox(
    "Select an Example Email",
    list(email_examples.keys()),
)

# Display the full text optionally (if you want the user to review)
st.text_area("Selected Email Content", email_examples[selected_label], height=500)

# Use selected email text for prediction
if st.button("Predict"):
    features = vectorizer.transform([email_examples[selected_label]])
    result = model.predict(features)[0]
    label = "✅ Ham (Safe Message)" if result == 1 else "⚠️ Spam/Phishing"
    st.write(f"**Prediction:** {label}")
