import streamlit as st

if "current_song" in st.session_state:
    st.image(image=st.session_state.current_song["album_cover"])

    title = st.session_state.current_song["title"]
    artist = st.session_state.current_song["artist"]

    st.header(title)
    st.subheader(artist)
else:
    st.subheader("You're currently playing... nothing.")
    st.page_link(page="pages/search_page.py", label="Go to Search to look for any song you like.")
    st.page_link(page="pages/sound_page.py", label="Or let us recognize a song you're hearing right now with berimBAM.")
# how to play music??
# Maybe make a skript search on YouTube for the name and song title and pick the first result to display?
