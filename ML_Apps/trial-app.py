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
        st.write("Data Head")
        st.write(df.head(5))
        st.write("Data Sample")
        st.write(df.sample(5))

        st.subheader("Data Summary")
        df = df.drop('Unnamed: 0', axis=1)
        df_describe = df.select_dtypes(['float64', 'int64']) #Filter Numeric Column
        # st.write(df_describe.describe())
        st.dataframe(df_describe.describe())

        st.write("Dataset Type")
        st.write(df.dtypes)

        st.write("Dataset Column")
        st.write(df.columns.tolist())

        st.write("Dataset Shapes")
        st.write(df.shape)

        st.subheader("Filter Data 🔍")
        cols=['result', 'team', 'venue', 'opponent', 'season']
        columns = df.columns.to_list()
        selected_column = st.selectbox("Select Column to filter by", cols)
        unique_val = df[selected_column].unique()
        selected_value = st.selectbox("Select Value", unique_val)

        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)

        st.subheader("Plot Data")
        x_col = st.selectbox("Select x-axis column", columns)
        y_col = st.selectbox("Select y-axis column", columns)

        if st.button("Generate Plot"):
            st.line_chart(filtered_df.set_index(x_col)[y_col])

    else:
        st.write("🕛 Waiting on file upload...")