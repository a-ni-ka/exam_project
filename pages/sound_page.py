import streamlit as st
from components.shazamio_helpers import process_sound

st.title("Let's berimBAM!")

audio_input = st.audio_input("Start recording to recognize a song...",
                             help="Accuracy increases if the audio snippet is 10 seconds or longer.")

# if a sound is recorded, it will run the function process sound from shazamio_helpers
if audio_input:
    # .read() function is used to convert the audio into byte format so shazamio can process the sound
    song = process_sound(audio_input.read())
    if song is not None:
        # if there is a result, user gets sent to the song page
        st.session_state.current_song = song
        st.switch_page("pages/song_page.py")
    else:
        st.write("Sorry, we couldn't find any matches for this song.")
