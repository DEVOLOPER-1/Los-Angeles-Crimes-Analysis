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




vict_sex_age_descent_crime_dataset = pd.read_csv("vict_age_sex_descent_crime.csv")



with st.container():
        st.title("vict_descent_relation_to_crime_activity")

        st.scatter_chart(
            data=vict_sex_age_descent_crime_dataset,
            y="victim_race",
            x="crime_against_the_victim",
        )


