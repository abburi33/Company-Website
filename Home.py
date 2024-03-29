import streamlit as st
import pandas as pd
from datetime import datetime
import smtplib
from email.message import EmailMessage
import config

# Email sender function
def send_email(subject, message, to_email):
    msg = EmailMessage()
    msg.set_content(message)
    msg['subject'] = subject
    msg['to'] = to_email
    msg['from'] = config.EMAIL_ADDRESS

    with smtplib.SMTP_SSL(config.SMTP_SERVER, config.SMTP_PORT) as smtp:
        smtp.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
        smtp.send_message(msg)

# Streamlit webpage layout
st.set_page_config(layout="wide")

# Header and content
st.header("Your Research Assisstant!")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(content)

# Meeting scheduling
st.subheader("Schedule a Meeting")

with st.form("meeting_form"):
    meeting_type = st.selectbox("Meeting Type:", ["Internal", "Client", "Team"])
    description = st.text_input("Description:")
    date = st.date_input("Date:", value=datetime.now())
    time = st.time_input("Time:", value=datetime.now().time())

    attendee_email = st.text_input("Attendee Email:")
    attendee_name = st.text_input("Attendee Name:")

    submitted = st.form_submit_button("Schedule")

    if submitted:
        # Combine date and time
        date_time = datetime.combine(date, time)
        
        # Send email
        subject = f"Meeting Scheduled: {meeting_type} - {description}"
        message = f"A {meeting_type} meeting is scheduled on {date_time.strftime('%Y-%m-%d %H:%M')} with {attendee_name}."
        send_email(subject, message, attendee_email)
        st.success("Meeting scheduled successfully!")

# Team information
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")
