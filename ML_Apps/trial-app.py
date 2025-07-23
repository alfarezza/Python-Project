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

        st.subheader("Data Summary")
        df = df.drop('Unnamed: 0', axis=1)
        df_describe = df.select_dtypes(['float64', 'int64']) #Filter Numeric Column
        # st.write(df_describe.describe())
        st.dataframe(df_describe.describe())

        st.caption("Dataset Type")
        st.write(df.dtypes)

        st.caption("Dataset Column")
        st.write(df.columns.tolist())

        st.caption("Dataset Shapes")
        st.write(df.shape)