import streamlit as st

phishing_detector = st.Page("phishing.py", title="Check for Phishing")
example_email = st.Page("Examples.py", title="Email Examples")
information_page = st.Page("information.py", title="How to detect a Phishing Email")

pg = st.navigation([phishing_detector, example_email, information_page])
st.set_page_config(page_title="Phishing Email Detector")
pg.run()
