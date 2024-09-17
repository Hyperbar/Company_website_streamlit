import streamlit as st
import pandas
from send_email import  send_email

df = pandas.read_csv(r"C:\Users\sztre\Desktop\dev\mes_projets\Company_website_streamlit\topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    option = st.selectbox(
        "What topic do you want to discuss?",
        df["topic"]
    )
    text_message = st.text_area("Text")
    message =f"""\
Subject: New email from {user_email}

From:{user_email}
Topic {option}
{text_message}
"""
    submit= st.form_submit_button("Submit")
    if submit:
        send_email(message)
        st.info("Your email has been sent successfully")

# Select box
# What topic do you want to discuss

# Text tex box

# Submit button
