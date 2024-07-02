import streamlit as st
import pandas as pd
import plotly.express as px


diff_date_bet_report_occurence_in_days_dataset = pd.read_csv(r"report_occurence.csv")

average_duration_to_report = round(
    diff_date_bet_report_occurence_in_days_dataset["differences"].mean()
)


with st.container():
        st.title(
            body="Time Gap between :red[Crime] Occurence and :red[Crime] Reporting in days"
        )
        st.subheader(
            f"Every crime might be discovered or reported after an average of :red[{average_duration_to_report} days]."
        )
        st.scatter_chart(
            diff_date_bet_report_occurence_in_days_dataset,
            x="differences",
            y="case_nuber",
            x_label="Date Difference bet. Occurence of crime and Reporting it in days scale",
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