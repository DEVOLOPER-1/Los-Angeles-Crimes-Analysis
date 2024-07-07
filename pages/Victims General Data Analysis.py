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

Age, Sex = st.columns(2, gap="medium")

crimes, races = st.columns(2, gap="medium")


Age_values_dict = dict(
    vict_sex_age_descent_crime_dataset["age"].value_counts(dropna=True)
)

print(Age_values_dict)


# Map the values from the dictionary to the DataFrame
vict_sex_age_descent_crime_dataset["value"] = vict_sex_age_descent_crime_dataset[
    "age"
].map(Age_values_dict)
with Age:
    with st.container():
        st.title(":red[Victims] Ages")
        st.subheader("Why are Some Ages :red[Targeted] More? ")

        fig = px.pie(vict_sex_age_descent_crime_dataset, names="age", values="value")
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("See explanation :point_down:"):
            st.write(
                """
        ## Age and Crime: Why Some Are More Vulnerable

Ever wonder why certain age groups seem like bigger targets for crime? Age plays a surprising role. While you might think older adults are most at risk, young adults (18-24) actually experience more violent crime. 

This vulnerability stems from factors like risk-taking behavior, lack of experience, and socioeconomic challenges.  However, age isn't the only story. Children are easily overpowered, while older adults might be targeted for financial scams. 

Understanding these patterns is key. It allows us to create targeted solutions. For young adults, this could be safety workshops. For children, it's about personal safety education and creating safe spaces. Protecting older adults might involve fighting financial scams and raising awareness. 

By tackling these vulnerabilities at different stages of life, we can build a safer future for everyone. 
        """
            )


sex_values_dict = dict(
    vict_sex_age_descent_crime_dataset["sex"].value_counts(dropna=True)
)

vict_sex_age_descent_crime_dataset["sex_count"] = vict_sex_age_descent_crime_dataset[
    "sex"
].map(sex_values_dict)

print(sex_values_dict)
with Sex:
    with st.container():
        st.title(":red[Victims] Sex")
        st.subheader(
            "What factors contribute to higher :red[victimization] rates among males for crimes? "
        )

        fig2 = px.pie(
            vict_sex_age_descent_crime_dataset,
            names="sex",
            values="sex_count",
            # color= ["#910A67" , "#720455" , "#3C0753" , "#030637"]
        )
        st.plotly_chart(fig2, use_container_width=True)
        with st.expander("See explanation :point_down:"):
            st.write(
                """
## Why Men Might Be More Likely Victims of Some Crimes

The numbers can be surprising: statistics often show more male victims of certain crimes compared to females.  While the reasons are complex, here's a quick look:

* **Types of Crime Matter:** Men are more likely to be victims of violent crimes like robbery and assault. This might be due to risk-taking behavior, being in high-crime areas, or physical altercations. Property theft can also target men more often. 
* **Reporting Can Be Unequal:**  Social stigma around male vulnerability might make men less likely to report crimes, especially sexual assault. Fear of retaliation can also be a factor.  
* **Domestic Violence Differs:** While domestic violence affects both genders, women are more likely to experience violence from intimate partners. 

"""
            )


race_values_dict = dict(
    vict_sex_age_descent_crime_dataset["victim_race"].value_counts(dropna=True)
)

vict_sex_age_descent_crime_dataset["victim_race_count"] = (
    vict_sex_age_descent_crime_dataset["victim_race"].map(race_values_dict)
)

with races:
    with st.container():
        st.title(":red[Victims] Race")
        st.subheader("Visualizing Victim Demographics")

        fig3 = px.pie(
            vict_sex_age_descent_crime_dataset,
            names="victim_race",
            values="victim_race_count",
            # color= ["#910A67" , "#720455" , "#3C0753" , "#030637"]
        )
        st.plotly_chart(fig3, use_container_width=True)
        with st.expander("See explanation :point_down:"):
            st.write(
                """ 
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
* **Z - Asian Indian:** Individuals of Asian Indian descent. 
                     """
            )


crimes_count_dict = dict(
    vict_sex_age_descent_crime_dataset["crime_against_the_victim"].value_counts(
        dropna=True
    )
)

vict_sex_age_descent_crime_dataset["crimes_count"] = vict_sex_age_descent_crime_dataset[
    "crime_against_the_victim"
].map(crimes_count_dict)


print(crimes_count_dict)


with crimes:
    with st.container():
        st.title("Acts of :red[crime]")
        st.subheader("Top :red[Crimes] on the Streets")

        fig4 = px.pie(
            vict_sex_age_descent_crime_dataset,
            names="crime_against_the_victim",
            values="crimes_count",
            # color= ["#910A67" , "#720455" , "#3C0753" , "#030637"]
        )
        st.plotly_chart(fig4, use_container_width=True)
