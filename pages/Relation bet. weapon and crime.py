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


df = pd.read_csv("weapon_code_df.csv")

crime_weapon, weapons_count = st.columns(2, gap="medium")


# Relation between the crime and weapon

with crime_weapon:
    with st.container():
        st.scatter_chart(
            data=df,
            y="crime_code_identifier",
            x="weapon_desc",
            x_label="Commited Crime",
            y_label="Used Weapon",
        )



weapons_count_dict = dict(df["weapon_desc"].value_counts())
df["weapon_used_counts"] = df["weapon_desc"].map(weapons_count_dict)

with weapons_count:
    with st.container():
        fig = px.pie(df, names="weapon_desc", values="weapon_used_counts")
        st.plotly_chart(fig, use_container_width=True)