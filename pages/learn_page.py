import streamlit as st

st.title("Learn about Capoeira")

tab1, tab2 = st.tabs(["Capoeira Theory", "The Bateria"])
with tab1:
    st.header("Capoeira Styles")
    with st.expander("Capoeira angola"):
        st.video("https://youtu.be/y2eLeiMaU1k")
        st.write("""
            'Capoeira Angola is played close to the ground. The movements are generally more theatrical and players 
            rely on their wit and trickery to outdo their opponents. Angola emphasizes tradition, African heritage, and 
            music far more than the other two styles. Most Angoleiros attempt to maintain the traditions of capoeira 
            and take pride in preserving the Afro-Brazilian art.'

            source: DendeArts (https://dendearts.com/the-different-styles-of-capoeira-full-explaination/)
            """)
    with st.expander("Capoeira regional"):
        st.video("https://youtu.be/zmw_0TRmNcY")
        st.write("""
            'Regional is the first widespread systemization of capoeira as a martial art in an academic setting. The 
            game of regional is more powerful, martial, and upright than Angola. There is much less of the 
            theatricality you might see in Angola, and all these differences stem from the system developed by Mestre 
            Bimba.'

            source: DendeArts (https://dendearts.com/the-different-styles-of-capoeira-full-explaination/)
            """)
    with st.expander("Capoeira contemporânea"):
        st.video("https://youtu.be/xFkYRCX2h9s", start_time=370)
        st.write("""
            'Contemporânea schools are defined by their evolution on the art of capoeira. They take elements of Angola 
            and Regional, and incorporate them into their unique style. Acrobatics, grappling, and advanced floreios 
            are some concepts that have been added by various Contemporânea schools. Unlike Judo, where a centralized 
            body controls every school through certifications and curriculum, capoeira schools operate almost 
            completely independently. 
            This means that most schools have the freedom to experiment and grow in a way that is unique.'

            source: DendeArts (https://dendearts.com/the-different-styles-of-capoeira-full-explaination/)
            """)

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
            socially ostracized for more than 40 years. Mestre Bimba, the legendary Capoeira Master, rescued the art 
            form and proved its legitimacy, opening capoeira’s first official school in Bahia, Brazil.

            Capoeira was born as an expression of resistance and resilience that brought spiritual and emotional 
            empowerment. The cultures of enslaved Africans, Brazilian indigenous peoples, and Portuguese immigrants 
            all contributed to the art of capoeira, and the art form is a reflection of the cultural and social 
            integration of the diverse people comprising modern-day Brazil.

            Capoeira has developed into a means of empowerment and a forum for social and cultural exchange. 
            It is now an internationally respected art of grace and strength that combines ritual, self-defense, 
            acrobatics, and music.'

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

            Mestre Pastinha was born on April 5, 1889, in Salvador, Bahia, Brazil. He is celebrated for his dedication 
            to preserving the traditional style of capoeira known as Capoeira Angola. Unlike the more modern Capoeira 
            Regional, Capoeira Angola emphasizes the playful and ritualistic elements of the martial art. 
            Pastinha opened the first official Capoeira Angola academy, called the Centro Esportivo de Capoeira Angola, 
            in 1942. His teachings focused on the philosophy, history, and techniques of capoeira, ensuring that its 
            African roots were honored. He passed away on November 13, 1981.

            source: Wikipedia (https://de.wikipedia.org/wiki/Mestre_Pastinha), summarized with help of Microsoft Copilot
            """)
with tab2:
    st.markdown("""
    ### In capoeira, the bateria is the term used for the group of instruments that accompany the roda with music.
    Depending on the group and style of capoeira, this assembly can look very different. Below you see the instruments
    that are most commonly found in a bateria de capoeira.
    """)
    with st.expander("Berimbau"):
        c1, c2 = st.columns(2)
        with c1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/6/67/Berimbau_parts.svg",
                     width=300,
                     caption="This file is licensed under the Creative Commons Attribution 3.0 Unported license.")
        with c2:
            st.markdown("""
            The **berimbau** is generally seen as the most important instrument in capoeira. It begins the music and 
            sets the style and rhythm for the roda.
            
            There are three types of berimbau:
            - **Gunga**: The Gunga has a deep and rich sound. It is the first instrument to play in a roda, and it 
            dictates the rhythm and tempo to all other instruments. The person who plays the Gunga is also responsible 
            for giving permission to the first two players of the roda to start their game.
            - **Médio**: The Médio has a clear and strong sound. It starts playing after the Gunga and complements
            the rhythm of the Gunga, but can also add some decorative rhythm elements every now and then.
            - **Viola**: The Viola has a bright and intense sound. It starts playing after the other two berimbaus and 
            can add a lot of decorative and improvised rhythms.
            """)
    with st.expander("Atabaque"):
        c3, c4 = st.columns(2)
        with c3:
            st.image("https://upload.wikimedia.org/wikipedia/commons/e/ee/Atabaque_in_the_street.jpg",
                     width=300,
                     caption="Picture by Xandu, Gemeinfrei, https://commons.wikimedia.org/w/index.php?curid=2327104")
        with c4:
            st.markdown("""
            The **atabaque** is a large drum made of hardwood and leather. A skilled player can produce a big dynamic
            variety of sound with this instrument. In a roda, the atabaque helps stabilize the rhythm of the berimbaus.
            It will usually start playing after the berimbaus, and usually, there will be only one atabaque used in a
            roda.
            """)
    with st.expander("Pandeiro"):
        c5, c6 = st.columns(2)
        with c5:
            st.image("https://upload.wikimedia.org/wikipedia/commons/6/65/Pandeiro.jpg",
                     width=300,
                     caption="This file is licensed under the Creative Commons Attribution 3.0 Unported license.")
        with c6:
            st.markdown("""
            The **pandeiro** is the Brazilian version of the tambourine. Apart from capoeira, it is also used in other
            traditional Brazilian music such as Samba. Most often, a bateria de capoeira will have one or two pandeiros.
            They usually start playing after the atabaque to complement the rhythm of the roda. The rhythm of the
            pandeiro can range from very simple to complex with occasional improvisation, depending on the skill of the
            musician.
            """)
    with st.expander("Agogô"):
        c7, c8 = st.columns(2)
        with c7:
            st.image("http://www.capoeira-erfurt.de/images/speasyimagegallery/albums/2/images/agogo.jpg",
                     width=300,
                     caption="©2025 Capoeira Berimbau Erfurt")
        with c8:
            st.markdown("""
            The **agogô** is a percussion instrument made of wood and two nut shells (for example Brazil Nut shells)
            that produce two clear, loud sounds - generally one higher and one lower. It complements the rhythm of the 
            roda and is usually the last instrument of the bateria to start playing. The simplest way to play the 
            agogô in a roda de capoeira is *low, high, low, pause* in sync with the pandeiros.
            """)
