import streamlit as st

placeholder = st.empty()

with placeholder.form("Login"):
    st.write("Please enter your login data. If you don't have an account yet, please click 'Register'.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.form_submit_button("Login")
    register_button = st.form_submit_button("Register")

    if register_button:
        st.switch_page("pages/registration_page.py")
