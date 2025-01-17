import streamlit as st

st.image(image=st.session_state.current_song["album_cover"])

title = st.session_state.current_song["title"]
artist = st.session_state.current_song["artist"]

st.header(title)
st.subheader(artist)
