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



with st.container():
        st.title("Victim Descent Relation to :red[Crime] Activity Against them")
        st.subheader("Why are Some Descents :red[Targeted] More? ")
        st.scatter_chart(
            data=vict_sex_age_descent_crime_dataset,
            y="victim_race",
            x="crime_against_the_victim",
            
            color= ["#A91D3A"]
        )
        with st.expander("See explanation :point_down:"):
            st.write("""
                     

### Why Some Descents Might Show Higher Crime Activity Against them ?


### Socioeconomic Factors
- **Poverty and Unemployment**: Higher poverty and unemployment rates often correlate with increased crime. When people struggle to meet their basic needs, they may turn to illegal activities.

### Geographical Factors
- **Urbanization and Neighborhoods**: Urban areas and certain neighborhoods can have higher crime rates due to higher population density, fewer resources, and less community cohesion.

### Social and Cultural Factors
- **Social Inequality**: Disparities in income, education, and access to services can lead to higher crime rates in marginalized communities.
- **Cultural Norms**: Cultural practices and community norms can sometimes influence crime rates.

### Historical Factors
- **Discrimination and Displacement**: Historical discrimination and forced migration can create long-term socioeconomic disadvantages, contributing to higher crime rates in certain groups.

### Law Enforcement Practices
- **Policing and Judicial Inequality**: Disproportionate targeting by law enforcement and disparities in the judicial system can lead to higher recorded crime rates and harsher sentencing for some groups.

### Access to Education and Services
- **Education and Social Services**: Limited access to quality education and social services, such as mental health care, can increase the likelihood of criminal activity.

### Community Factors
- **Community Cohesion and Youth Engagement**: Strong social networks can lower crime rates, while lack of engagement and opportunities for youth can lead to higher juvenile crime rates.

### Conclusion
The reasons behind higher crime activity in certain descents are complex and multifaceted. Addressing these issues requires a comprehensive approach, including collaboration with community leaders and detailed data analysis, to identify and tackle the root causes effectively.

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


""")

