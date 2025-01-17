import streamlit as st
from components.database import connect_to_collection

profile_image = None


@st.dialog("Edit your profile")
def edit_profile():
    global profile_image
    profile_image = st.file_uploader("Upload a profile image", type=["png", "jpg", "jpeg"])
    nickname = st.text_input("Your nickname:")
    group = st.text_input("Your group:")
    grade = st.text_input("Your grade:")
    city = st.text_input("What city are you in?")
    save_button = st.button("Save changes")
    cancel_button = st.button("Cancel", type="primary")
    if save_button:
        document = {
            "nickname": nickname,
            "group": group,
            "grade": grade,
            "city": city
        }
        profile_collection.insert_one(document)


if not st.session_state.credentials_check:
    st.subheader("You are not logged in.")
    st.page_link(page="pages/login_page.py", label="Log in to see your Profile.")

if st.session_state.credentials_check:
    profile_collection = connect_to_collection("berimbam", "profile_data")
    edit_button = st.button("Edit Profile", icon=":material/settings:", on_click=edit_profile)
    st.subheader("Your Profile")
    if profile_image is None:
        st.image(image="images/profile_pic.png", width=150)

