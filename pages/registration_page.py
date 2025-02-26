import streamlit as st
import pandas as pd
import datetime as dt
from components.database import connect_to_collection


@st.dialog("Registration successful")
# create a dialog window after a successful registration
def register():
    st.write("You can now log in.")
    continue_button = st.button("Continue")
    if continue_button:
        st.switch_page("pages/login_page.py")


placeholder = st.empty()

# create a form in the st.empty container
with placeholder.form("Registration"):
    username = st.text_input("Username*", placeholder="Your username")
    email = st.text_input("E-Mail*", placeholder="example@mail.com")
    password = st.text_input("Password*", type="password", placeholder="Your password")
    repeat_password = st.text_input("Repeat Password*", type="password", placeholder="Repeat password")
    submit_button = st.form_submit_button("Register")

    if submit_button:
        # define the database
        db_name = 'berimbam'
        # define the collection
        collection_name = 'login_data'
        collection = connect_to_collection(db_name, collection_name)

        # read the data from the collection and identify usernames
        user_data = pd.DataFrame(list(collection.find()))
        usernames = list(user_data.username)
        if username in usernames:
            st.error("Username taken", icon="⚠️")
        elif len(username) < 1 and len(password) < 1:
            st.error("Please enter user name and password", icon="⚠️")
        elif len(username) < 1:
            st.error("Please enter a user name", icon="⚠️")
        elif len(password) < 1:
            st.error("Please enter a password", icon="⚠️")
        elif len(email) < 1:
            st.error("Please enter your email address", icon="⚠️")
        elif repeat_password != password:
            st.error("Passwords do not match", icon="⚠️")
        else:
            # if all conditions are met, create a document containing the data to add to the collection
            document = {
                "username": username,
                "email": email,
                "password": password,
                "created_at": dt.datetime.now()
            }
            collection.insert_one(document)
            register()
