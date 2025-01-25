import base64
import pandas as pd
import streamlit as st
from components.database import connect_to_collection

profile_image = None


@st.dialog("Edit your profile")
def edit_profile():
    global profile_image
    image = st.file_uploader("Upload a profile image", type=["png", "jpg", "jpeg"])
    if image:
        encoded_image = base64.b64encode(image.read())
    else:
        # with help of https://www.askpython.com/python/examples/encoding-image-with-base64
        with open("images/profile_pic.png", "rb") as file:
            encoded_image = base64.b64encode(file.read())
    nickname = st.text_input("Your nickname:")
    group = st.text_input("Your group:")
    title = st.selectbox(
        "Your title:",
        ("student", "advanced", "Professor/-a", "Contramestre/-a", "Mestre/-a"),
        index=None,
        placeholder="Select your current title"
    )
    city = st.text_input("What city are you in?")
    save_button = st.button("Save changes")
    cancel_button = st.button("Cancel", type="primary")
    if save_button:
        document = {
            "user": st.session_state.user,
            "profile_pic": encoded_image,
            "nickname": nickname,
            "group": group,
            "title": title,
            "city": city
        }
        profile_collection.update_one(
            {"user": st.session_state.user},
            {"$set": document},
            upsert=True
        )
        st.rerun()
    if cancel_button:
        st.rerun()


if not st.session_state.credentials_check:
    st.subheader("You are not logged in.")
    st.page_link(page="pages/login_page.py", label="Log in to see your Profile.")

if st.session_state.credentials_check:
    edit_button = st.button("Edit Profile", icon=":material/settings:", on_click=edit_profile)
    st.subheader("Your Profile")

    profile_collection = connect_to_collection("berimbam", "profile_data")
    profile_data = pd.DataFrame(list(profile_collection.find()))
    users = list(profile_data.user)
    if st.session_state.user in users:
        profile_pic = base64.b64decode(list(profile_data[profile_data.user == st.session_state.user].profile_pic)[0])
        st.image(profile_pic, width=200)
        st.write(f"Apelido: {list(profile_data[profile_data.user == st.session_state.user].nickname)[0]}")
        st.write(f"Group: {list(profile_data[profile_data.user == st.session_state.user].group)[0]}")
        st.write(f"Current Title: {list(profile_data[profile_data.user == st.session_state.user].title)[0]}")
        st.write(f"Located in: {list(profile_data[profile_data.user == st.session_state.user].city)[0]}")
    else:
        st.image(image="images/profile_pic.png", width=150)
        st.write("Click 'Edit Profile' to add some information about yourself.")
