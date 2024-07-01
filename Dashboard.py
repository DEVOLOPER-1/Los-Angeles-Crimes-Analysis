import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import statistics

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
                        
                        ## Why the Gap Between Crime and Report?

Ever notice how news reports sometimes seem delayed after a crime? There's a reason for that! Here's the scoop:

* **People Hold Back:** Victims or witnesses might wait to report due to fear, shock, or simply needing time.
* **Investigations Take Time:** Complex crimes or those requiring evidence collection can't be rushed. 
* **Death Investigations are Special:** Determining cause of death and sifting through a missing person case add extra layers of complexity.

## Why Still Report a Crime?

Even if time has passed, reporting a crime is vital:

* **Justice Doesn't Have a Deadline:** Delayed reports can help solve cold cases or ongoing crimes. 
* **Helping Victims Heal:** Reporting can connect victims with resources and support. 
* **Safer Communities:** Crime patterns help law enforcement understand and prevent future crimes.

So, if you've been a victim or witness to a crime, know this: reporting it, whenever you're ready, makes a difference. It helps bring criminals to justice, supports victims, and keeps our communities safer. 
                        
 """
            )

with crime_code_with_description:
    with st.container():
        st.write("col2")

with mocodes_analysis:
    with st.container():
        st.write("col3")
