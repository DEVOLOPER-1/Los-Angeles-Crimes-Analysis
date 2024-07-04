import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk


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



df = pd.read_csv("precise_time_df.csv")

count_times_dict = dict(df["hr_min_time"].value_counts())

df["count_time"] = df["hr_min_time"].map(count_times_dict)

with st.container():
        fig = px.pie(df, names="hr_min_time", values="count_time")
        st.plotly_chart(fig, use_container_width=True)