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


df = pd.read_csv("crimes_area_codes_df.csv")

areas_count_dict = dict(df["area_name"].value_counts())

df["areas_counts"] = df["area_name"].map(areas_count_dict)

with st.container():
    st.title("Most :red[Crime] Areas")
    st.subheader("Identifying Crime :red[Hotspots]")

    fig = px.pie(df, names="area_name", values="areas_counts")
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("See explanation :point_down:"):
        st.write(
            """
                     ## Why Do Certain Areas Become Crime Hotspots?

Ever wonder why some neighborhoods seem to experience more crime? It's not a random thing. Crime hotspots form due to a complex mix of social and economic factors.

**The Recipe for Trouble:**

Imagine a recipe for crime. Poverty, lack of opportunity, and crumbling buildings are like the ingredients. When these elements mix, they can create an environment where crime seems like the only option for some. Broken windows and a lack of community spirit further weaken the recipe, making it easier for crime to take root.

**Opportunity Knocks for Criminals:**

Think of crime as needing three things: a motivated criminal, a vulnerable target, and an absence of someone watching. In hotspots, these elements often find themselves in the same place at the same time. Plus, certain businesses like bars or pawn shops can attract criminals due to the potential for trouble.

**Location:**

Crime hotspots aren't randomly scattered. Busy areas like transportation hubs can be prime pickpocketing spots due to the anonymity. Neighborhoods in flux, with rapid population changes, might lack the social connections that keep crime in check.

**But There's Hope!**

The good news? Crime hotspots aren't permanent. By tackling the root causes like poverty and social disorganization, we can create a recipe for strong, safe communities. 
                     
                     """
        )


with st.container():
    st.title("Mapping :red[Crime] Distribution Areas with Associated Codes")
    st.subheader(":red[Crime] Clusters sizes varies by crimes counts")

    st.scatter_chart( data= df , 
                     x = "area" , 
                     y = "area_name" , 
                     size= "areas_counts",
                     color="#5D0E41")

    with st.expander("See explanation :point_down:"):
        st.write(
            """
        
                     ## Why Do Certain Areas Become Crime Hotspots?

Ever wonder why some neighborhoods seem to experience more crime? It's not a random thing. Crime hotspots form due to a complex mix of social and economic factors.

**The Recipe for Trouble:**

Imagine a recipe for crime. Poverty, lack of opportunity, and crumbling buildings are like the ingredients. When these elements mix, they can create an environment where crime seems like the only option for some. Broken windows and a lack of community spirit further weaken the recipe, making it easier for crime to take root.

**Opportunity Knocks for Criminals:**

Think of crime as needing three things: a motivated criminal, a vulnerable target, and an absence of someone watching. In hotspots, these elements often find themselves in the same place at the same time. Plus, certain businesses like bars or pawn shops can attract criminals due to the potential for trouble.

**Location:**

Crime hotspots aren't randomly scattered. Busy areas like transportation hubs can be prime pickpocketing spots due to the anonymity. Neighborhoods in flux, with rapid population changes, might lack the social connections that keep crime in check.

**But There's Hope!**

The good news? Crime hotspots aren't permanent. By tackling the root causes like poverty and social disorganization, we can create a recipe for strong, safe communities. 
                     
                                         
                     
                     
                     """
        )
