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


df = pd.read_csv("weapon_code_df.csv")

# crime_weapon, weapons_count = st.columns(2, gap="medium")


# Relation between the crime and weapon

# with crime_weapon:
with st.container():
    st.title("Fist Fight or Firearm? Why Crime Type Dictates the :red[Weapon] Choice ")
    st.subheader("Unveiling the criminal's weapon playbook.")
    st.scatter_chart(
        data=df,
        y="crime_code_identifier",
        x="weapon_desc",
        x_label="Commited Crime",
        y_label="Used Weapon",
        color="#A91D3A",
    )

    with st.expander("See explanation :point_down:"):
        st.write(
            """
                     ## Crooks Got Choices: Why They Don't All Pack Heat

Think every crook walks around with a gun? Think again! Criminals gotta pick the right tool for the job, just like you wouldn't use a hammer to open a soda. Here's the lowdown:

* **Need a Smash? Grab a Bash:** Breaking into a store? A crowbar's your best friend. Big score planned? Maybe a gun comes out to play. The weapon gotta match the crime, whether it's a quiet scare or stopping someone cold. 

* **Fight Night or Pickpocket Hustle?** Not all crimes involve a beatdown. A sneaky thief uses smooth moves, not a knife. But an angry attacker might use fists or a club to get in your face. The weapon choice depends on how much violence is on the menu.

* **Risk vs. Reward: Think Before You Thwack!** Criminals don't want cops chasing them. A gun might seem cool, but it also brings major heat. For a quick steal, something less obvious keeps things smooth.

* **Weaponry by Accident:** Sometimes, it's all about what's around. A heated moment might end with a broken bottle, or the criminal grabs whatever's close. 
                     """
        )


weapons_count_dict = dict(df["weapon_desc"].value_counts())
df["weapon_used_counts"] = df["weapon_desc"].map(weapons_count_dict)

# with weapons_count:
with st.container():
    st.title("Beyond Bullets: Unveiling the Arsenal of Criminals")
    st.subheader(
        "From everyday objects to high-tech tools, we explore the surprising underworld of criminal :red[weaponry]."
    )
    fig = px.pie(df, names="weapon_desc", values="weapon_used_counts")
    st.plotly_chart(fig, use_container_width=True)
    with st.expander("See explanation :point_down:"):
        st.write(
            """
                     ## knowing the most common crime weapons can be your secret weapon for:

* **Dodgeball in the Real World:** You'll be spotting threats like a pro, from everyday objects to surprising picks. Think of it as pre-crime awareness, keeping you two steps ahead. 

* **Fact vs. Fiction Smackdown:** Forget Hollywood's gun-obsessed bad guys. This knowledge debunks myths and lets you focus on the real threats out there. 

* **Crime Scene: Your Neighborhood:** Knowing what criminals favor lets you take preventative measures. Think home security upgrades or extra vigilance in high-risk areas. 

* **Power Up for Law Enforcement:**  Cops and security forces use this intel to identify threats faster, understand criminal intent, and be prepared for anything. 

* **Public Policy with a Punch:** This data shapes discussions on gun control, violence prevention, and how to train our protectors. 
                     
                     
                     """
        )
