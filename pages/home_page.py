import streamlit as st
import datetime as dt
from components.shazamio_helpers import search_songs

greeting_options_list = [
    "Good morning", "Good afternoon",
    "Good evening", "Seize the night"
]
greeting = ""

time = dt.datetime.now().time()

if 5 <= time.hour < 12:
    greeting = greeting_options_list[0]
elif 12 <= time.hour < 18:
    greeting = greeting_options_list[1]
elif 18 <= time.hour < 24:
    greeting = greeting_options_list[2]
elif time.hour < 5:
    greeting = greeting_options_list[3]

if not st.session_state.credentials_check:
    st.markdown(f"**:rainbow[{greeting}!]**")
else:
    st.markdown(f"**:rainbow[{greeting}, {st.session_state.user}!]**")

st.title("Home")

song_1 = search_songs("sou jogador mestre barrao")[0]
song_2 = search_songs("boa voz berimbau viola")[0]
song_3 = search_songs("quem vem la mestre suassuna")[2]
song_4 = search_songs("capoeira nago")[0]

with st.container():
    st.subheader("Top songs")
    r1c1, r1c2, r1c3, r1c4 = st.columns(4)
    with r1c1:
        st.image(song_1["album_cover"], width=160)
        button_1 = st.button(f"{song_1["title"]} by {song_1["artist"]}")
        if button_1:
            st.session_state.current_song = song_1
            st.switch_page("pages/song_page.py")
    with r1c2:
        st.image(song_2["album_cover"], width=160)
        button_2 = st.button(f"{song_2["title"]} by {song_2["artist"]}")
        if button_2:
            st.session_state.current_song = song_2
            st.switch_page("pages/song_page.py")
    with r1c3:
        st.image(song_3["album_cover"], width=160)
        button_3 = st.button(f"{song_3["title"]} by {song_3["artist"]}")
        if button_3:
            st.session_state.current_song = song_3
            st.switch_page("pages/song_page.py")
    with r1c4:
        st.image(song_4["album_cover"], width=160)
        button_4 = st.button(f"{song_4["title"]} by {song_4["artist"]}")
        if button_4:
            st.session_state.current_song = song_4
            st.switch_page("pages/song_page.py")

with st.container():
    st.subheader("Popular Playlists")
    r2c1, r2c2, r2c3, r2c4, r2c5 = st.columns(5)
    r2c1.write("placeholder2")
    r2c2.write("placeholder2")
    r2c3.write("placeholder2")
    r2c4.write("placeholder2")
    r2c5.write("placeholder2")
