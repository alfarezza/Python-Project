import streamlit as st
import pandas as pd
import joblib
import os
import datetime
import warnings
import sklearn
import cloudpickle

warnings.filterwarnings("ignore", message=".*use_column_width.*")

# ================================= Page =================================
st.set_page_config(page_title="ML-Apps", page_icon="🤖", layout="wide")

# @st.cache_resource
# def load_model():
#     model_path = ""
#     if not os.path.exists(model_path):
#         raise FileNotFoundError(f"⚠️ Model Not Found at {model_path}")
#     with open(model_path, "rb") as f:
#         return cloudpickle.load(f)
    
# model = load_model()

st.sidebar.title("📂 Main Menu!")
page = st.sidebar.radio('Choose Page:', ['Prediction', 'Data Understanding', 'Exploratory Data Analysis', 'About Me'])

# ================================= Prediction Page =================================
if page == 'Prediction':
    st.header("🖥️ Input Data!")
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            gender = st.selectbox['Gender', ['Male', 'Female']]
        with col2:
            age = st.slider("Age (Year):", 17, 80, 25)