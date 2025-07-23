import streamlit as st

def aboutme():
    st.header("🤵 Alfarezza Ryan P. Purba")

    col1, col2 = st.columns([2,1]) #ratio 2:1

    with col1:
        st.markdown(
            """
            <div style='text-align: justify;'>
            Hi, I’m a junior <b>Data Scientist</b> 🧠📊 who’s seriously passionate about turning data into insights. I love running experiments on datasets (sometimes to the point of giving myself a headache 🤯 because I get that excited).
            From exploring big data and learning the latest IT tools, to analyzing complex problems and building compelling presentations 🎯—I’m all in. I'm always curious, constantly learning, and genuinely enjoy the process of uncovering patterns, building models, and telling data-driven stories.
            I’ve worked with tools like <b>Python, Jupyter Notebook, SSMS, and Power BI</b> 📈, and I’m confident in both wrangling data and presenting it in a way that makes sense to everyone—from tech teams to stakeholders. 
            Whether it’s writing clean code 👨‍💻, building dashboards 📊, or pitching ideas backed by solid data, I’m always looking to level up and make an impact through data 🚀.
            <br><br>
            👉 Feel free to explore this portfolio to see some of my work and skills in action. I hope it gives you a clear picture of what I’m capable of as a data scientist, and how passionate I am about this field!<br>
            💬 I’m always open to feedback or suggestions on my projects—after all, every comment is a chance to grow and improve!<br>
            🔗 Let’s connect on LinkedIn if you’d like to collaborate, chat about data, or just say hi!
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")
        st.subheader("📬 Contact & Profile")
        st.markdown("- 📧 Email: alfarezza08@gmail.com")
        st.markdown("- 💼 [LinkedIn](https://www.linkedin.com/in/alfarezza-ryan/)")
        st.markdown("- 🐙 [GitHub](https://github.com/alfarezza)")
        # st.markdown("- 🌐 [Website](https://.com/)")

    with col2:
        st.image("logo\github-mark.png", width=500, caption="Alfarezza Ryan P. Purba")  # Ganti dengan foto profil atau logo