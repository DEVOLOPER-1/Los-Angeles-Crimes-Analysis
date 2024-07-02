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


df = pd.read_csv('crimes_area_codes_df.csv')

areas_count_dict = dict(df["area_name"].value_counts())

df["areas_counts"] = df[
    "area_name"
].map(areas_count_dict)

with st.container():
        st.title("Most :red[Crime] Areas")
        st.subheader("")

        fig = px.pie(df, names="area_name", values="areas_counts")
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("See explanation :point_down:"):
            st.write("")


