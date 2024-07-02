import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(
    page_title="Los Angeles Crimes",
    page_icon=":collision:",
    layout="wide",  # To Use the entire screen as we want
    initial_sidebar_state="auto",
    menu_items={
        "About": "https://www.linkedin.com/in/youssef-mohammad-9341a71a7",
        "Get help": "https://github.com/DEVOLOPER-1",
    },
)

df = pd.read_csv(
    r"C:\Users\youss\OneDrive\سطح المكتب\Kaggle\cleaned_df.csv", low_memory=False
)


st.header(body="Los Angeles Crimes :gun:", divider="red", anchor=False)

vict_sex_age_descent_crime_dataset = pd.read_csv("vict_age_sex_descent_crime.csv")





