import streamlit as st
from send_mail import send_mail

st.header("Contact Us")

with st.form(key="company_form"):
    user_email = st.text_input("Your Email Address")
    topic = st.selectbox(
        "What topic do you want to discuss?",
        ("Job Inquiries", "Project Proposals", "Other")
    )
    text = st.text_area("Text")
    submit_button = st.form_submit_button("Submit")
    message = f"""\
Subject: New mail from {user_email}

From: {user_email}
topic: {topic}
message: {text}
"""
    if submit_button:
        send_mail(message)
        st.info("Your email was sent successfully")

