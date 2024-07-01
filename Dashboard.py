import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime


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

diff_date_bet_report_occurence_in_days_dataset = pd.read_csv(r"report_occurence.csv")

st.header(body="Los Angeles Crimes :gun:", divider="red", anchor=False )


(
    diff_date_bet_report_occurence_in_days,
    crime_code_with_description,
    mocodes_analysis,
) = st.columns(3, gap="medium")

count = 0

average_duration_to_report = round(diff_date_bet_report_occurence_in_days_dataset["differences"].mean())

with diff_date_bet_report_occurence_in_days:
    with st.container():
        st.title(body = "Time Gap between :red[Crime] Occurence and :red[Crime] Reporting")
        st.subheader(f"Every crime might be discovered or reported after an average of :red[{average_duration_to_report} days].")
        st.scatter_chart(
            diff_date_bet_report_occurence_in_days_dataset,
            x="differences",
            y="case_nuber",
            x_label="Date Difference bet. Occurence of crime and Reporting it in days",
            y_label="Case Number",
            color=["#5D0E41"],  # ,"A0153E"]
        )
        with st.expander("See explanation :point_down:"):
            st.write(
                """
                        
                        ## Crimes Don't Always Hit Reports Right Away

Police records can lag behind actual crimes. Here's why:

* **People Hesitate:** Fear, shock, or confusion can delay reporting.
* **Investigations Take Time:** Complex cases need thorough investigation before entering the system.
* **Death Investigations Are Slower:** Scene checks, autopsies, and missing person verifications add time.

But even late reports matter:

* **Cold Case Solvers:** Past crimes can crack unsolved cases.
* **Victim Help:** Reports connect victims with support resources.
* **Crime Prevention:** Patterns help police understand and prevent future crimes.

So report a crime whenever you're ready - it makes a difference! 

 """
            )

with crime_code_with_description:
    with st.container():
        st.write("col2")

with mocodes_analysis:
    with st.container():
        st.write("col3")
