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


st.header(body="Los Angeles Crimes :gun:", divider="red", anchor=False)


(
    diff_date_bet_report_occurence_in_days,
    crime_code_with_description,
    mocodes_analysis,
) = st.columns(3, gap="medium")

count = 0

with diff_date_bet_report_occurence_in_days:
    with st.container():
        st.write("col1")
        date_reported = df["date_reported"].to_list()
        print(date_reported[0])
        date_occured = df["date_occured"].to_list()
        print(date_occured[1])

        cases_numbers = []
        differences = []

        for reported, occured in zip(date_reported, date_occured):
            if reported != "nan" and occured != "nan":

                try:
                    date_time_obj_r = datetime.strptime(reported, "%m/%d/%Y %I:%M:%S %p")

                    date_time_obj_o = datetime.strptime(occured, "%m/%d/%Y %I:%M:%S %p")

                    year_diff = abs(date_time_obj_r.year - date_time_obj_o.year)

                    month_diff = abs(date_time_obj_r.month - date_time_obj_o.month)

                    day_diff = abs(date_time_obj_r.day - date_time_obj_o.day)

                    total_diff_in_days = day_diff + (month_diff * 30) + (year_diff * 365)

                    differences.append(total_diff_in_days)
                    
                    count+=1
                except:
                    count+=1
                    print(f"bad format {count}")


        for index, row in df.iterrows():
            case_num = row["division_of_records"]
            case_num = str(case_num)
            case_num = case_num[4:9]
            cases_numbers.append(case_num)
            
        diff_date_bet_report_occurence_in_days_df = pd.DataFrame({'x': cases_numbers, 'y': differences})
   
        st.line_chart( data= diff_date_bet_report_occurence_in_days_df , x='x', y='y', x_label='None', y_label='None',use_container_width=True)

print(len(differences) , len(cases_numbers))
days_average = statistics.mean(differences)
print(days_average)
with crime_code_with_description:
    with st.container():
        st.write("col2")

with mocodes_analysis:
    with st.container():
        st.write("col3")
