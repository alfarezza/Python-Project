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
            I’ve worked with tools like Python, Jupyter Notebook 📓, SSMS 🗄️, and Power BI 📈, and I’m confident in both wrangling data and presenting it in a way that makes sense to everyone—from tech teams to stakeholders. 
            Whether it’s writing clean code 👨‍💻, building dashboards 📊, or pitching ideas backed by solid data, I’m always looking to level up and make an impact through data 🚀.
            
            👉 Feel free to explore this portfolio to see some of my work and skills in action. I hope it gives you a clear picture of what I’m capable of as a data scientist, and how passionate I am about this field!
            💬 I’m always open to feedback or suggestions on my projects—after all, every comment is a chance to grow and improve!
            🔗 Let’s connect on LinkedIn if you’d like to collaborate, chat about data, or just say hi!


            Saya adalah lulusan <b>Teknik Informatika</b> yang memiliki minat besar di bidang <b>Data Science</b>. 
            Memiliki pengalaman kerja di bidang Administrasi, Komunikasi, dan Jaringan, yang erat kaitannya dengan industri IT, 
            saya terbiasa bekerja secara analitis dan terstruktur.
            <br><br>
            Saya terus mengembangkan kemampuan melalui berbagai bootcamp intensif dan sertifikasi, 
            sebagai bentuk komitmen terhadap pembelajaran berkelanjutan.
            <br><br>
            Tujuan karier saya adalah menjadi <b>Data Scientist</b> yang mampu menghadirkan insight berbasis data 
            dan mendukung pengambilan keputusan strategis yang berdampak langsung pada pertumbuhan bisnis.
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