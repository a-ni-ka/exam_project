import streamlit as st

placeholder = st.empty()

with placeholder.form("Registration"):
    username = st.text_input("Username*", placeholder="Your username")
    email = st.text_input("E-Mail*", placeholder="example@mail.com")
    birth_date = st.date_input("Birth Date", value=None)
    password = st.text_input("Password*", type="password", placeholder="Your password")
    repeat_password = st.text_input("Repeat Password*", type="password", placeholder="Repeat password")
    submit_button = st.form_submit_button("Register")

    if submit_button:
        # if username in usernames:
        #     st.error("Username taken", icon="⚠️")
        if len(username) < 1 and len(password) < 1:
            st.error("Please enter user name and password", icon="⚠️")
        elif len(username) < 1:
            st.error("Please enter a user name", icon="⚠️")
        elif len(password) < 1:
            st.error("Please enter a password", icon="⚠️")
        elif len(email) < 1:
            st.error("Please enter your email address", icon="⚠️")
        elif repeat_password != password:
            st.error("Passwords do not match", icon="⚠️")
