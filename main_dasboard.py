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

(
    diff_date_bet_report_occurence_in_days,
    vict_descent_relation_to_crime_activity,  # crime_code_with_description
    vict_sex_age_descent_crime_section,  # monocodes analysis
) = st.columns(3, gap="medium")

count = 0



with vict_descent_relation_to_crime_activity:
    with st.container():
        st.title("vict_descent_relation_to_crime_activity")

        st.scatter_chart(
            data=vict_sex_age_descent_crime_dataset,
            y="victim_race",
            x="crime_against_the_victim",
        )



