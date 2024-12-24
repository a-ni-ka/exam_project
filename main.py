import streamlit as st

st.set_page_config(page_title="berimBAM Web",
                   page_icon="images/app_icon.png")

pages = {
    "Navigate": [
        st.Page("pages/home_page.py", title="🏠 Home"),
        st.Page("pages/sound_page.py", title="🎙️ berimBAM"),
        st.Page("pages/search_page.py", title="🔎 Search"),
        st.Page("pages/learn_page.py", title="📖 Learn"),
        st.Page("pages/profile_page.py", title="👤 Profile")
    ]
}

pg = st.navigation(pages)
pg.run()

# home, listen, search, learn, profile = st.tabs(["🏠", "🎙️", "🔎", "📖", "👤"])
