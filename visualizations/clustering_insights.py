import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Clustering Insights - Automotive Cybersecurity")

# Initial Feature: DBSCAN Clustering
st.header("Clustering of Attack Types")
data = pd.DataFrame({
    "Attack_Type": ["DoS", "Fuzzy", "Spoofing", "Replay"],
    "Frequency": [120, 80, 95, 60],
    "Cluster": [0, 1, 0, 1],
})
fig1 = px.scatter(
    data,
    x="Attack_Type",
    y="Frequency",
    color="Cluster",
    title="DBSCAN Clustering of Attack Types"
)
st.plotly_chart(fig1)
st.write(
    "This scatter plot uses DBSCAN to cluster attack types. It identifies patterns between attack frequencies, "
    "helping prioritize defenses for frequent clusters."
)

# New Visualization: Regional Comparison
st.header("Regional Attack Analysis")
region_data = pd.DataFrame({
    "Region": ["North America", "Europe", "Asia", "South America"],
    "DoS": [40, 50, 70, 30],
    "Fuzzy": [30, 20, 40, 10],
    "Spoofing": [20, 30, 50, 20],
})
fig2 = px.bar(
    region_data,
    x="Region",
    y=["DoS", "Fuzzy", "Spoofing"],
    labels={"value": "Frequency", "variable": "Attack Type"},
    title="Comparison of Attack Types by Region",
    barmode="group"
)
st.plotly_chart(fig2)
st.write(
    "This bar graph compares the frequency of different attack types across regions. Asia shows the highest attack "
    "frequencies, indicating the need for regional cybersecurity focus."
)