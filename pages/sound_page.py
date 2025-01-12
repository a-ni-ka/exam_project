import streamlit as st
from st_click_detector import click_detector
# custom component by vivien: https://github.com/vivien000/st-click-detector


def get_sound():
    placeholder.empty()
    placeholder.audio_input("Recording...",
                            help="If the recording doesn't auto-start, click the mic icon.")


placeholder = st.empty()

with placeholder.container():
    st.title("Click to recognize a song")
    image = """
    <a href='#' id='sound'>
    <img width='60%' src='https://raw.githubusercontent.com/a-ni-ka/exam_project/refs/heads/main/images/app_icon.png'></a>
    """
    clicked = click_detector(image)

    if clicked == "sound":
        get_sound()
