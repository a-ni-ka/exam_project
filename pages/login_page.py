import streamlit as st
import pandas as pd
from components.database import connect_to_collection


placeholder = st.empty()

with placeholder.form("Login"):
    st.write("Please enter your login data. If you don't have an account yet, please click 'Register'.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.form_submit_button("Login")
    register_button = st.form_submit_button("Register")

    if login_button:
        db_name = "berimbam"
        collection_name = "login_data"
        collection = connect_to_collection(db_name, collection_name)

        # check username
        # read the data from the collection and identify usernames
        user_data = pd.DataFrame(list(collection.find()))
        usernames = list(user_data.username)

        # check password
        if username in usernames:
            # this selects the password of the user that is entering information
            registered_password = list(user_data[user_data.username == username].password)[0]

            if password == registered_password:
                st.session_state.credentials_check = True
                st.switch_page("pages/home_page.py")
            else:
                st.error("The username/password is not correct")
        else:
            st.error("Please provide correct user name or click on register as new user")

    if register_button:
        st.switch_page("pages/registration_page.py")
