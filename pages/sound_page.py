import streamlit as st

st.title("Click to recognize song")

st.button("ಥ_ಥ")

button_html = """
<img src='images/app_icon.png' style='width:100px;height:60px;'>
"""

st.markdown(button_html, unsafe_allow_html=True)
