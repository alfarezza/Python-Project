import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ================================= Page =================================
st.set_page_config(page_title="Trial-Apps", page_icon="🤖", layout="wide")

st.title("Simple Data Dashboard 📊")

# ================================= Side Menu =================================
st.sidebar.title("📂 Main Menu!")
page = st.sidebar.radio('Choose Page:', ['Data Understanding', 'Exploratory Data Analysis', 'About Me'])


# ================================= Menu Data Understanding =================================
if page == 'Data Understanding':
    load_file = st.file_uploader("Choose a CSV file", type="csv")

    if load_file is not None:
        df = pd.read_csv(load_file)

        st.subheader("Data Preview 📅")
        st.write(df.head(10))
