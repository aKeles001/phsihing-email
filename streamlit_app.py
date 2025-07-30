import streamlit as st

create_page = st.Page("phishing.py", title="Check for Phishing")
delete_page = st.Page("Examples.py", title="Email Examples")
information_page = st.Page("information.py", title="How to detect a Phishing Email")

pg = st.navigation([create_page, delete_page, information_page])
st.set_page_config(page_title="Data manager")
pg.run()
