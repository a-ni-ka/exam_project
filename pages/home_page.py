import streamlit as st
import datetime as dt

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

st.markdown(f"**:rainbow[{greeting}!]**")

st.title("Home")

with st.container():
    st.subheader("Top songs")
    r1c1, r1c2, r1c3, r1c4, r1c5 = st.columns(5)
    r1c1.write("placeholder1")
    r1c2.write("placeholder1")
    r1c3.write("placeholder1")
    r1c4.write("placeholder1")
    r1c5.write("placeholder1")

with st.container():
    st.subheader("Popular Playlists")
    r2c1, r2c2, r2c3, r2c4, r2c5 = st.columns(5)
    r2c1.write("placeholder2")
    r2c2.write("placeholder2")
    r2c3.write("placeholder2")
    r2c4.write("placeholder2")
    r2c5.write("placeholder2")
