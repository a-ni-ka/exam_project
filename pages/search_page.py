import streamlit as st
from components.shazamio_helpers import search_songs

st.title("Search")

search = st.text_input("Search for songs, artists, albums...", placeholder="🔎 What are you looking for?")

container = st.empty()

if search:
    song_list = search_songs(search)
    for song in song_list:
        result_button = st.button(label=f"{song['title']} by {song['artist']}")
        if result_button:
            st.session_state.current_song = song
            st.switch_page("pages/song_page.py")
