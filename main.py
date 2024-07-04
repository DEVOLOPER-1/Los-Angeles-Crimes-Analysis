import streamlit as st
import pandas as pd
import plotly.express as px
import time


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


st.header(body="Los Angeles Crimes :gun:", divider="red", anchor=False)


story = """
## The Importance of Crime Analysis in Los Angeles: A Story

## Imagine it's a typical evening in Los Angeles. Jane, a young professional, is walking home after a long day at work. As she approaches her apartment, she notices a few police cars in the vicinity :police_car:. Concerned, she checks her phone for any news updates.

## Jane remembers hearing about a new dashboard that provides detailed analysis of crime records in Los Angeles. Curious and a bit anxious, she decides to explore it. Upon visiting the dashboard, she is immediately drawn in by its intuitive interface and the wealth of information available.

## The dashboard reveals the crime trends in her neighborhood over the past year :bar_chart:. She learns about the most common types of crimes, the times they are likely to occur, and even the areas with the highest crime rates. This information is not only eye-opening but also empowers her to make informed decisions about her safety and daily routines :mag_right:.

## Jane finds out that the area near her home has seen a recent increase in theft incidents. She takes note of the safety tips provided on the dashboard and decides to share this valuable resource with her friends and family, ensuring they stay informed as well :globe_with_meridians:.

## The analysis doesn't just stop at identifying crime trends. The dashboard also highlights the efforts of local law enforcement and community initiatives aimed at reducing crime. Jane feels a sense of relief knowing that steps are being taken to make her city safer :shield:.

## For Jane and countless others in Los Angeles, this dashboard is more than just a tool; it's a lifeline. It provides critical insights that help residents stay vigilant and contribute to a safer community. Discover the power of crime analysis and take control of your safety with our comprehensive dashboard today! :star2:
"""


story_list = []
for word in story.split(" "):
    story_list.append(word)


def stream_data(story_list):
    for word in story_list:
        yield word
        time.sleep(0.5)


stream_data(story_list)


# Create a placeholder for the text
placeholder = st.empty()

# Initialize an empty string to hold the streamed text
streamed_text = ""

# Stream the story
for word in stream_data(story_list):
    streamed_text += word + " "
    placeholder.markdown(streamed_text)
