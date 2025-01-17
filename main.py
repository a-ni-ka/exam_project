import streamlit as st

st.set_page_config(page_title="berimBAM Web",
                   page_icon="images/app_icon.png")

# also set up a credential check
if 'credentials_check' not in st.session_state:
    st.session_state.credentials_check = False

if not st.session_state.credentials_check:
    pages = {
        "Navigate": [
            st.Page("pages/home_page.py", title="🏠 Home"),
            st.Page("pages/sound_page.py", title="🎙️ berimBAM"),
            st.Page("pages/search_page.py", title="🔎 Search"),
            st.Page("pages/learn_page.py", title="📖 Learn"),
            st.Page("pages/profile_page.py", title="👤 Profile"),
            st.Page("pages/song_page.py", title="")
        ],
        "Your Account": [
            st.Page("pages/login_page.py", title="Log in"),
            st.Page("pages/registration_page.py", title="Create Account")
        ]
    }
else:
    pages = {
        "Navigate": [
            st.Page("pages/home_page.py", title="🏠 Home"),
            st.Page("pages/sound_page.py", title="🎙️ berimBAM"),
            st.Page("pages/search_page.py", title="🔎 Search"),
            st.Page("pages/learn_page.py", title="📖 Learn"),
            st.Page("pages/profile_page.py", title="👤 Profile")
        ]
    }
    with st.sidebar:
        log_out_button = st.button("Log out", type="primary")
        if log_out_button:
            st.session_state.credentials_check = False
            st.rerun(scope="app")

with st.sidebar.popover("About berimBAM"):
    st.write("This app was created by a-ni-ka on GitHub as a project for Leuphana University Lüneburg, Germany.")

st.logo(image="images/app_logo.png", size="large", icon_image="images/app_icon.png")
pg = st.navigation(pages)
pg.run()
