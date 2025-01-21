import streamlit as st

if "current_song" in st.session_state:
    st.image(image=st.session_state.current_song["album_cover"])

    title = st.session_state.current_song["title"]
    artist = st.session_state.current_song["artist"]

    st.header(title)
    st.subheader(artist)
else:
    st.subheader("Nothing to see here")
# how to play music??
# Maybe make a skript search on YouTube for the name and song title and pick the first result to display?
