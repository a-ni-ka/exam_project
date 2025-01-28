import streamlit as st

st.title("Learn about Capoeira")

tab1, tab2, tab3 = st.tabs(["Rhythm excercise", "Berimbau practice", "Capoeira Theory"])
with tab1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/65/Pandeiro.jpg")
    st.button("Get started")
with tab2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/67/Berimbau_parts.svg",
             width=300,
             caption="This file is licensed under the Creative Commons Attribution 3.0 Unported license.")
    st.button("Practice Berimbau")
with tab3:
    st.header("Capoeira Styles")
    with st.expander("Capoeira angola"):
        st.video("https://youtu.be/y2eLeiMaU1k")
    with st.expander("Capoeira regional"):
        st.video("https://youtu.be/zmw_0TRmNcY")
    with st.expander("Capoeira contemporânea"):
        st.video("https://youtu.be/xFkYRCX2h9s")

    st.header("Capoeira History")
    with st.expander("The origins of Capoeira"):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Rugendasroda.jpg/1200px-Rugendasroda.jpg",
                 width=500,
                 caption="This file is licensed under the Creative Commons Attribution 3.0 Unported license.")
        st.write("""
        'Capoeira developed as a result of more than three hundred years of slavery in Brazil. 
        Enslaved Africans were taken by Portuguese colonists from various cultures in Africa. 
        In Brazil, generations of enslaved African people shared the cultural customs, dances, rituals, 
        and fighting techniques that would combine to become capoeira. Slaves used capoeira to fight to escape 
        and resist capture, but concealed its combative purpose through music, song, and dance.

        Even after the abolition of slavery in Brazil in 1888, capoeira was illegal and its practitioners were 
        socially ostracized for more than 40 years. Mestre Bimba, the legendary Capoeira Master, rescued the art form 
        and proved its legitimacy, opening capoeira’s first official school in Bahia, Brazil.

        Capoeira was born as an expression of resistance and resilience that brought spiritual and emotional empowerment. 
        The cultures of enslaved Africans, Brazilian indigenous peoples, and Portuguese immigrants all contributed 
        to the art of capoeira, and the art form is a reflection of the cultural and social integration of the diverse 
        people comprising modern-day Brazil.

        Capoeira has developed into a means of empowerment and a forum for social and cultural exchange. 
        It is now an internationally respected art of grace and strength that combines ritual, self-defense, acrobatics,
         and music.'

        source: Abadá Capoeira (https://www.abada.org/capoeira-history/)
        """)
    with st.expander("About Mestre Bimba"):
        st.image("https://upload.wikimedia.org/wikipedia/en/d/d2/Mestre_Bimba.jpeg",
                 width=300,
                 caption="This file is licensed under the Creative Commons Attribution 3.0 Unported license.")
        st.write("""
        Birth name: Manuel dos Reis Machado (November 23, 1900 – February 5, 1974)
        
        Mestre Bimba is known as the founder of one of the most practised styles of Capoeira: capoeira regional, 
        a style which modernized capoeira by incorporating more martial techniques and making it more effective. 
        He is credited with being a major contributor to the legalization of Capoeira in Brazil in 1937, 
        and in that same year officially registered the nation's first Capoeira center.
        Bimba was born on November 23, 1900, in Salvador, Bahia, Brazil. He began learning capoeira at age 12 
        and later developed his own style to counter the perception of capoeira as merely a dance or ritual. 
        He introduced new kicks and movements, and emphasized teaching capoeira to a broader audience, 
        which helped in its decriminalization. Bimba was also an accomplished singer and berimbau player. 
        He passed away on February 5, 1974, leaving a lasting legacy in the world of capoeira.
        
        source: Wikipedia (https://en.wikipedia.org/wiki/Manuel_dos_Reis_Machado), 
        summarized with help of Microsoft Copilot
        """)
    with st.expander("About Mestre Pastinha"):
        st.image("https://upload.wikimedia.org/wikipedia/en/0/0d/Mestre_Pastinha.jpg",
                 width=300,
                 caption="This file is licensed under the Creative Commons Attribution 3.0 Unported license.")
        st.write("""
        Birth name: Vicente Ferreira Pastinha (April 5, 1889 - November 13, 1981)
        
        Mestre Pastinha was born on April 5, 1889, in Salvador, Bahia, Brazil. He is celebrated for his dedication to 
        preserving the traditional style of capoeira known as Capoeira Angola. Unlike the more modern Capoeira Regional,
         Capoeira Angola emphasizes the playful and ritualistic elements of the martial art. 
        Pastinha opened the first official Capoeira Angola academy, called the Centro Esportivo de Capoeira Angola, 
        in 1942. His teachings focused on the philosophy, history, and techniques of capoeira, ensuring that its 
        African roots were honored. He passed away on November 13, 1981.
        
        source: Wikipedia (https://de.wikipedia.org/wiki/Mestre_Pastinha), summarized with help of Microsoft Copilot
        """)
