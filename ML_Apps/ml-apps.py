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