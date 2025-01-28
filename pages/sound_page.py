import streamlit as st
from components.shazamio_helpers import process_sound

st.title("Let's berimBAM!")

audio_input = st.audio_input("Start recording to recognize a song...",
                             help="Accuracy increases if the audio snippet is 10 seconds or longer.")

if audio_input:
    st.session_state.current_song = process_sound(audio_input.read())
    if st.session_state.current_song is not None:
        st.switch_page("pages/song_page.py")
    else:
        st.write("Sorry, we couldn't find any matches for this song.")
