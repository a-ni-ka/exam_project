import streamlit as st
from components.shazamio_helpers import search_songs

st.title("Search")

search = st.text_input("Search for songs, artists, albums...", placeholder="🔎 What are you looking for?")

if search:
    search_songs(search)
