import streamlit as st
# from st_click_detector import click_detector
# custom component by vivien: https://github.com/vivien000/st-click-detector
from components.shazamio_helpers import process_sound


# def get_sound():
#     placeholder.empty()
#     audio_input = st.audio_input("Recording...",
#                                  help="If the recording doesn't auto-start, click the mic icon.")
#     return audio_input


audio_input = st.audio_input("Start recording to recognize song...",
                             help="Accuracy increases if the audio snippet is 10 seconds or longer.")

if audio_input:
    st.session_state.current_song = process_sound(audio_input.read())
    if st.session_state.current_song is not None:
        st.switch_page("pages/song_page.py")
    else:
        st.write("Sorry, we couldn't find any matches for this song.")

# placeholder = st.empty()

# with placeholder.container():
#     st.title("Click to recognize a song")
#     image = """
#     <a href='#' id='sound'>
#     <img width='60%' src='https://raw.githubusercontent.com/a-ni-ka/exam_project/refs/heads/main/images/app_icon.png'></a>
#     """
#     clicked = click_detector(image)
#
#     if clicked == "sound":
#         sound = get_sound()
#         if sound:
#             process_sound(sound)
