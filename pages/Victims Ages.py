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
    },)



vict_sex_age_descent_crime_dataset = pd.read_csv("vict_age_sex_descent_crime.csv")

values_dict  = dict(vict_sex_age_descent_crime_dataset["age"].value_counts(dropna = True) )

print(values_dict)

# Map the values from the dictionary to the DataFrame
vict_sex_age_descent_crime_dataset['value'] = vict_sex_age_descent_crime_dataset['age'].map(values_dict)

with st.container():
        st.title("Victim Ages")
        st.subheader("Why are Some Ages :red[Targeted] More? ")
        
        fig = px.pie(vict_sex_age_descent_crime_dataset, names='age',values= 'value')
        st.plotly_chart(
                fig,
                use_container_width = True
        )