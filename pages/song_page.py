import streamlit as st

if "current_song" in st.session_state:
    # display the current_song
    st.image(image=st.session_state.current_song["album_cover"])

    st.audio(data=st.session_state.current_song["preview"])

    title = st.session_state.current_song["title"]
    artist = st.session_state.current_song["artist"]

    st.header(title)
    st.subheader(artist)
else:
    # if there's no current_song in the session state, a placeholder text will be displayed
    st.subheader("You're currently playing... nothing.")
    st.page_link(page="pages/search_page.py", label="Go to Search to look for any song you like.")
    st.page_link(page="pages/sound_page.py", label="Or let us recognize a song you're hearing right now with berimBAM.")
