import base64
import pandas as pd
import streamlit as st
from components.database import connect_to_collection


@st.dialog("Edit your profile")
# an st.dialog function will open a dialog window
def edit_profile():
    image = st.file_uploader("Upload a profile image", type=["png", "jpg", "jpeg"])
    if image:
        # to upload an image to the database, we have to encode it/convert it to string
        encoded_image = base64.b64encode(image.read())
    else:
        # with help of https://www.askpython.com/python/examples/encoding-image-with-base64
        with open("images/profile_pic.png", "rb") as file:
            encoded_image = base64.b64encode(file.read())
    nickname = st.text_input("Your nickname:", max_chars=25)
    about = st.text_input("About you:", max_chars=150, help="Write a short bio to let others know more about you. 🤗")
    group = st.text_input("Your group:", max_chars=30)
    title = st.selectbox(
        "Your title:",
        ("student", "advanced", "Professor/-a", "Contramestre/-a", "Mestre/-a"),
        index=None,
        placeholder="Select your current title"
    )
    city = st.text_input("What city is your group in?")
    save_button = st.button("Save changes")
    cancel_button = st.button("Cancel", type="primary")
    if save_button:
        # if you click save, the data will be stored in a document
        document = {
            "user": st.session_state.user,
            "profile_pic": encoded_image,
            "nickname": nickname,
            "about": about,
            "group": group,
            "title": title,
            "city": city
        }
        # update the user's profile document or create one if it doesn't exist yet
        profile_collection.update_one(
            {"user": st.session_state.user},
            {"$set": document},
            upsert=True
        )
        # rerun the page to close the dialog window after clicking save
        st.rerun()
    if cancel_button:
        # closes the dialog window without saving your changes
        st.rerun()


if not st.session_state.credentials_check:
    # this appears if you visit the page while not logged in
    st.subheader("You are not logged in.")
    st.page_link(page="pages/login_page.py", label="Log in to see your Profile.")

if st.session_state.credentials_check:
    # this appears if you visit the page while logged in
    edit_button = st.button("Edit Profile", icon=":material/settings:", on_click=edit_profile)
    st.subheader("Your Profile")

    # connect to the database to find the user's profile data
    profile_collection = connect_to_collection("berimbam", "profile_data")
    profile_data = pd.DataFrame(list(profile_collection.find()))
    users = list(profile_data.user)
    if st.session_state.user in users:
        # if there's a document for the user, the profile data will be displayed
        # the encoded picture from the database is decoded to be displayed normally
        profile_pic = base64.b64decode(list(profile_data[profile_data.user == st.session_state.user].profile_pic)[0])
        st.image(profile_pic, width=200)
        st.markdown(f"""        
        **Apelido:** {list(profile_data[profile_data.user == st.session_state.user].nickname)[0]}
        
        **Current Title:** {list(profile_data[profile_data.user == st.session_state.user].title)[0]}
        
        **About me:** {list(profile_data[profile_data.user == st.session_state.user].about)[0]}
        
        **Group:** {list(profile_data[profile_data.user == st.session_state.user].group)[0]}
        
        **Located in:** {list(profile_data[profile_data.user == st.session_state.user].city)[0]}
""")
        if "current_song" in st.session_state:
            st.markdown(f"**I'm currently listening to:** "
                        f"{st.session_state.current_song["title"]} by {st.session_state.current_song["artist"]}")
    else:
        st.image(image="images/profile_pic.png", width=150)
        st.write("Click 'Edit Profile' to add some information about yourself.")
