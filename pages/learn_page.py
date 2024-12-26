import streamlit as st

st.title("Learn stuff")

placeholder = st.empty()

with placeholder:
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.write("image of a pandeiro")
        st.button("Get started")
    with c2:
        st.write("image of a berimbau")
        st.button("Practice Berimbau")
    with c3:
        st.write("image of an atabaque")
        st.button("Let's go")
    with c4:
        st.write("history lesson")
        st.button("Learn more")
