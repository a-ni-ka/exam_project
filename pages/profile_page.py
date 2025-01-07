import streamlit as st

if not st.session_state.credentials_check:
    st.subheader("You are not logged in.")
    st.page_link(page="pages/login_page.py", label="Log in to see your Profile.")

if st.session_state.credentials_check:
    st.subheader("Your Profile")

