import streamlit as st

st.title("Learn about Capoeira")

tab1, tab2, tab3 = st.tabs(["Rhythm excercise", "Berimbau practice", "Capoeira Theory"])
with tab1:
    st.write("image of a pandeiro")
    st.button("Get started")
with tab2:
    st.write("image of a berimbau")
    st.button("Practice Berimbau")
with tab3:
    st.header("Capoeira Styles")
    with st.expander("Capoeira angola"):
        st.video("https://youtu.be/y2eLeiMaU1k")
    with st.expander("Capoeira regional"):
        st.video("https://youtu.be/zmw_0TRmNcY")
    with st.expander("Capoeira contemporânea"):
        st.write(" ")
    st.header("Capoeira History")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Rugendasroda.jpg/1200px-Rugendasroda.jpg",
             width=300)
    with st.expander("The origins of Capoeira"):
        st.write("""
        'Capoeira developed as a result of more than three hundred years of slavery in Brazil. Enslaved Africans were taken by Portuguese colonists from various cultures in Africa. In Brazil, generations of enslaved African people shared the cultural customs, dances, rituals, and fighting techniques that would combine to become capoeira. Slaves used capoeira to fight to escape and resist capture, but concealed its combative purpose through music, song, and dance.

        After the abolition of slavery in Brazil in 1888, capoeira was illegal and its practitioners were socially ostracized for more than 40 years. Mestre Bimba, the legendary Capoeira Master, rescued the art form and proved its legitimacy, opening capoeira’s first official school in Bahia, Brazil, in 1932.

        Capoeira was born as an expression of resistance and resilience that brought spiritual and emotional empowerment. The cultures of enslaved Africans, Brazilian indigenous peoples, and Portuguese immigrants all contributed to the art of capoeira, and the art form is a reflection of the cultural and social integration of the diverse people comprising modern-day Brazil.

        Capoeira has developed into a means of empowerment and a forum for social and cultural exchange. It is now an internationally respected art of grace and strength that combines ritual, self-defense, acrobatics, and music.'

        source: Abadá Capoeira (https://www.abada.org/capoeira-history/)
        """)
    st.image("https://upload.wikimedia.org/wikipedia/en/d/d2/Mestre_Bimba.jpeg",
             width=300)
    with st.expander("About Mestre Bimba"):
        st.write("""
        Birth name: Manuel dos Reis Machado (November 23, 1900 – February 5, 1974)
        
        Mestre Bimba is known as the founder of one of the most practised styles of Capoeira: capoeira regional. He is credited with being a major contributor to the legalization of Capoeira in Brazil in 1937, and in that same year officially registered the nation's first Capoeira center.
        """)
    st.image("https://upload.wikimedia.org/wikipedia/en/0/0d/Mestre_Pastinha.jpg",
             width=300)
    with st.expander("About Mestre Pastinha"):
        st.write("""
        
        """)
