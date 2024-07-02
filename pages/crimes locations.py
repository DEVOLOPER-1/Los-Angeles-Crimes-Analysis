import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk


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


df = pd.read_csv("crimes_locations_df.csv")

crimes_count_dict = dict(df["crime_code_identifier"].value_counts())

df["crimes_counts"] = df["crime_code_identifier"].map(crimes_count_dict)




with st.container():
    # st.title("Most :red[Crime] Areas")
    # st.subheader("Identifying Crime :red[Hotspots]")

    st.pydeck_chart(
        pdk.Deck(
            #map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=df['lat'].mean(),  # Center the map on the mean latitude
                longitude=df['lon'].mean(),  # Center the map on the mean longitude
                zoom=11,
                pitch=50,
                
            ),
            layers=[
                pdk.Layer(
                    'HexagonLayer',
                    data=df,
                    get_position='[lon, lat]',
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                    auto_highlight=True
                    
                ),
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df,
                    get_position='[lon, lat]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=800,
                    get_elevation = 'crimes_counts'
                    
                ),
            ],
        ),
        use_container_width=True
    )
    
    with st.expander("See explanation :point_down:"):
        st.write("")