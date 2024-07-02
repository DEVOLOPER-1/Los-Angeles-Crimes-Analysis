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

st.header(body="Los Angeles Crimes :gun:", divider="red", anchor=False)

vict_sex_age_descent_crime_dataset = pd.read_csv("vict_age_sex_descent_crime.csv")

(
    diff_date_bet_report_occurence_in_days,
    crime_code_with_description,
    vict_sex_age_descent_crime_section,  # monocodes analysis
) = st.columns(3, gap="medium")

count = 0

average_duration_to_report = round(
    diff_date_bet_report_occurence_in_days_dataset["differences"].mean()
)

with diff_date_bet_report_occurence_in_days:
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

with crime_code_with_description:
    with st.container():
        st.write("col2")

with vict_sex_age_descent_crime_section:
    with st.container():
        st.title("4D Exploration: Victim Sex, Race, :red[Crime] Type by Age")
        st.subheader("Explore below the :red[Crime Data] for Yourself ")
        
        color_map = {
        "F": "#00224D",
        "M": "#5D0E41",
        "X": "#A0153E",
        "H": "#151515"
    }

    # Apply this mapping to your data (assuming `sex` has categories)
        vict_sex_age_descent_crime_dataset['color'] = vict_sex_age_descent_crime_dataset['sex'].map(color_map)
        fig = px.scatter_3d(
            vict_sex_age_descent_crime_dataset,
            x="sex",
            y="victim_race",
            z="crime_against_the_victim",
            size="age",
            #color_discrete_map= color_map
        )
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with st.expander("See explanation :point_down:"):
            st.write("""
                     
## Visualizing Diversity:

Imagine a four-dimensional world! We use a similar concept to represent our data. The first three dimensions explore **sex**, victim race (referring to their ethnic background), and the type of crime experienced. The final, fascinating dimension takes age into account, with the size of each data point reflecting the victim's age. This allows us to see trends and patterns across different demographics and age groups, creating a rich tapestry of information.

## Sex:

* **F:** Female
* **M:** Male
* **X:** Unknown
* **H:** Unavailable (This category can be omitted if not applicable to your data)

## Victim Race Codes:

* **A - Other Asian:** Individuals of Asian descent not otherwise specified.
* **B - Black:** Individuals of African descent. 
* **C - Chinese:** Individuals of Chinese descent.
* **D - Cambodian:** Individuals of Cambodian descent.
* **F - Filipino:** Individuals of Filipino descent.
* **G - Guamanian:** Individuals of Guamanian descent.
* **H - Hispanic/Latin/Mexican:** Individuals of Hispanic, Latino, or Mexican origin.  
* **I - American Indian/Alaskan Native:** Individuals of American Indian or Alaskan Native descent.
* **J - Japanese:** Individuals of Japanese descent.
* **K - Korean:** Individuals of Korean descent.
* **L - Laotian:** Individuals of Laotian descent.
* **O - Other:** Individuals of a race or ethnicity not otherwise specified.
* **P - Pacific Islander:** Individuals of Pacific Islander descent not otherwise specified.
* **S - Samoan:** Individuals of Samoan descent.
* **U - Hawaiian:** Individuals of Hawaiian descent.
* **V - Vietnamese:** Individuals of Vietnamese descent.
* **W - White:** Individuals of European descent.
* **X - Unknown:** Race or ethnicity is unknown.
* **Z - Asian Indian:** Individuals of Asian Indian descent. """ )