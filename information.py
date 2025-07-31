import streamlit as st

st.title("🔐 How to Identify and Spot Phishing Emails")

st.write("""
Phishing emails are one of the most common and misleading ways cybercriminals attempt to steal personal information, financial details, or credentials. These emails often appear legitimate and are crafted to trick recipients into taking harmful actions.

Whether you're a casual internet user or an experienced professional, learning to recognize phishing emails can protect you from serious financial and data loss.
""")

st.header("📧 What is a Phishing Email?")
st.write("""
A phishing email is a fraudulent message designed to trick you into revealing sensitive information such as:
- Passwords
- Credit card numbers
- Social Security Numbers

These emails may impersonate banks, online retailers, or even colleagues.
""")

st.header("💡 Why Do Phishing Emails Work?")
st.image("media/Success.png", caption="Why Do Phishing Emails Work?")
st.write("""
Phishing emails exploit human psychology using:
- **Urgency or fear** (e.g., "Your account will be locked!")
- **Excitement** (e.g., "You won a prize!")
- **Legitimate appearance** (e.g., logos, familiar formatting)

They are crafted to bypass your logical thinking by mimicking trusted sources.
""")

st.header("🎯 Common Phishing Techniques")
st.image("media/Techniques.png", caption="Common Phishing Techniques")
st.markdown("""
- **Email Spoofing** – Forging sender addresses to appear legitimate  
- **Social Engineering** – Pretending to be someone trustworthy  
- **Malware Delivery** – Sending malicious attachments or links
""")

st.header("🚨 How to Recognize a Phishing Email")
st.subheader("1. Check the Email Address")
st.write("""Phishers often hide their real email addresses to look like they’re from reputable sources. Pay attention to slight variations in the sender's email address.
""")
st.markdown("""
- ✅ Legit: `support@amazon.com`  
- ❌ Phish: `support@amaz0n-security.com`
""")

st.subheader("2. Suspicious or Generic Greeting")
st.write("""Phishing emails often use a generic greeting such as “Dear Customer” or “Dear User” because the attacker does not know your actual Name or Gender.""")
st.markdown("""
- ✅ Legit: “Dear John Doe”  
- ❌ Phish: “Dear Customer”
""")

st.subheader("3. Sense of Urgency or Threat")
st.write("""Phishing emails often create a sense of urgency or fear to prompt quick action. For example, they might threaten that your account will be locked unless you take action immediately, or you risk losing a reward.""")
st.markdown("""
- ✅ Legit: “Please review your account when convenient.”  
- ❌ Phish: “Click now to avoid account suspension!”
""")

st.subheader("4. Suspicious Links or Attachments")
st.write("""Phishing emails often include suspicious links or attachments designed to install malware on your device or steal your information. Hover over any link to check its destination URL.""")
st.markdown("""
Hover before clicking.  
- ✅ Legit: `https://www.amazon.com`  
- ❌ Phish: `http://malicious-site.com`
""")

st.subheader("5. Grammar and Spelling Mistakes")
st.write("""Many phishing emails contain noticeable spelling or grammatical errors. These can often be overlooked, but paying attention to these small mistakes can help you recognize a phishing email.""")
st.markdown("""
- ✅ Legit: Clear, professional language  
- ❌ Phish: “Your accunt is suspecious.”
""")

st.subheader("6. Unsolicited Requests for Personal Information")
st.write("""Phishing emails often ask you to provide sensitive information, such as login credentials, credit card details, or personal information.""")
st.markdown("""
- ✅ Legit: Never asks for sensitive info via email  
- ❌ Phish: “Please confirm your username and password.”
""")

st.subheader("7. Too Good to Be True Offers")
st.write("""If an email promises you something that seems too good to be true (like a large sum of money or an unbelievable discount), it’s probably a phishing attempt. Phishers use attractive offers to lure you into clicking a malicious link.""")
st.markdown("""
- ✅ Legit: Reasonable discounts  
- ❌ Phish: “You've won $1,000,000!”
""")

st.header("🛠️ Advanced Techniques to Spot Phishing")
st.write("""For more advanced users, identifying phishing attempts may involve examining headers and using tools to detect malicious emails.""")
st.subheader("1. Examine the Email Header")
st.write("""The email header provides information about the sender, path of the message, and more. By analyzing the header, you can check if the email has come from a legitimate source.""")
st.markdown("""
Check for:
- **Return-Path** mismatches  
- **SPF/DKIM** failures
""")

st.subheader("2. Use Anti-Phishing Tools")
st.write("""Most email providers, including Gmail, Outlook, and Yahoo, have built-in spam filters that can help identify phishing attempts. Additionally, tools like PhishTool or Email Verification Services can assist in validating the sender and authenticity of the email.""")
st.markdown("""
- Gmail, Outlook, Yahoo have spam filters  
- Third-party tools: PhishTool, EmailVeritas
""")

st.subheader("3. Verify Through Official Channels")
st.write("""If an email from a bank, service, or friend seems suspicious, always verify through official channels. For example, don’t click on the links in the email—go to the official website directly and log into your account to check for any updates.""")
st.markdown("""
Don’t trust links—visit the site manually via your browser.
""")
st.image("media/Guide.png", caption="How to Spot a Phishing Email")
st.header("📌 Real-World Phishing Email Examples")

with st.expander("Example 1: Fake Bank Alert"):
    st.code("""
Subject: Action Required: Secure Your Account Now  
From: security@fakebank.com  
Body: Click here to avoid being locked out!  
Link: www.fakebankaccountverify.com
""", language="text")

with st.expander("Example 2: Free iPhone Scam"):
    st.code("""
Subject: You’ve Won a Free iPhone!  
From: promotions@randomstuff.com  
Body: Claim your prize now!  
Link: suspicious-url.com
""", language="text")

st.header("✅ Conclusion")
st.write("""
Identifying phishing emails is key to staying safe online.  
**Beginners:** Watch for red flags like strange addresses, urgency, or grammar mistakes.  
**Advanced users:** Analyze email headers, use filtering tools, and always verify via official websites.

Stay cautious, think twice before clicking, and when in doubt — don’t trust, verify!
""")

st.markdown("---")
st.markdown(
    "<p style='font-size: 14px;'>"
    "🔗 <b>Source:</b> <a href='https://www.geeksforgeeks.org/techtips/how-to-identify-phishing-emails/' target='_blank'>"
    "GeeksforGeeks – How to Identify Phishing Emails</a><br>"
    "This guide includes insights adapted from the original article for educational use."
    "</p>",
    unsafe_allow_html=True
)

