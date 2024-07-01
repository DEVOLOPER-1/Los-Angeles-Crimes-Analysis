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


st.header(body="Los Angeles Crimes :gun:", divider="red", anchor=False)


(
    diff_date_bet_report_occurence_in_days,
    crime_code_with_description,
    mocodes_analysis,
) = st.columns(3, gap="medium")

with diff_date_bet_report_occurence_in_days:
    with st.container():
        st.write("col1")
        date_reported = df["date_reported"].to_list()
        print(date_reported[0])
        date_occured = df["date_occured"]
        print(date_occured[1])
        division_of_records_list = df["division_of_records"].to_list()
        print(division_of_records_list[0])
        cases_numbers = []
        differences = []

        for reported, occured in zip(date_reported, date_occured):
            # if reported != 'nan' and occured != 'nan':

            #     # Example date-time string
            #     date_time_str = "03/01/2020 12:00:00 AM"

            #     # Parse the date-time string to a datetime object
            #     date_time_obj_r = datetime.strptime(reported, "%m/%d/%Y %I:%M:%S %p")
                
            #     date_time_obj_o = datetime.strptime(occured,"%m/%d/%Y %I:%M:%S %p")
                
            #     # Print the datetime object
            #     print(date_time_obj_r)
                
            #     print(date_time_obj_o)

            #     # Example operations:
            #     # Get the year
            #     print("Year:", date_time_obj_r.year)

            #     # Get the month
            #     print("Month:", date_time_obj_r.month)

            #     # Get the day
            #     print("Day:", date_time_obj_r.day)
                
                
                
            #     print("Year:", date_time_obj_o.year)

            #     # Get the month
            #     print("Month:", date_time_obj_o.month)

            #     # Get the day
            #     print("Day:", date_time_obj_o.day)

   
        #         if reported[0:2] == occured[0:2] and reported[6:10] == occured[6:10]:
        #             difference = int(reported[3:5]) - int(occured[3:5])
        #             differences.append(difference)

        #         # This condition is made if the crime was reported after couple of monthes

        #         elif reported[0:2] != occured[0:2] and reported[6:10] == occured[6:10]:
        #             diff_bet_months = int(reported[0:2]) - int(occured[0:2])
        #             difference = (
        #                 int(reported[3:5]) - int(occured[3:5]) + (diff_bet_months * 30)
        #             )
        #             differences.append(difference)

        #         elif reported[0:2] != occured[0:2] and reported[6:10] != occured[6:10]:
        #             diff_bet_months = int(reported[0:2]) - int(occured[0:2])
        #             diff_bet_years = int(reported[6:10]) - int(occured[6:10])
        #             difference = (
        #                 int(reported[3:5])
        #                 - int(occured[3:5])
        #                 + (diff_bet_months * 30)
        #                 + (diff_bet_years * 365)
        #             )
        #             differences.append(difference)

            for value in division_of_records_list:
                    if isinstance(value, float):
                        print(f"Unexpected float value: {value}")
                #print(type(value))
                # case_num = int(value[4:9])
                # cases_numbers.append(case_num)


with crime_code_with_description:
    with st.container():
        st.write("col2")

with mocodes_analysis:
    with st.container():
        st.write("col3")
