import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Anomaly Detection in Automotive Systems")

# Initial Feature: Isolation Forest Anomalies
st.header("Detected Anomalies")
data = pd.DataFrame({
    "Timestamp": pd.date_range("2024-01-01", periods=100),
    "Frequency": [1 if i % 10 == 0 else 0 for i in range(100)],
    "Anomaly_Type": ["DoS" if i % 10 == 0 else "Normal" for i in range(100)],
})
fig1 = px.scatter(
    data,
    x="Timestamp",
    y="Frequency",
    color="Anomaly_Type",
    title="Anomalies Detected Using Isolation Forest"
)
st.plotly_chart(fig1)
st.write(
    "This scatter plot visualizes anomalies detected using Isolation Forest. Spikes in the plot indicate potential "
    "cyber-attacks requiring further investigation."
)

# New Visualization: Attack Distribution Across Components
st.header("Attack Distribution by Car Component")
component_data = pd.DataFrame({
    "Component": ["Engine", "Transmission", "Brakes", "Steering"],
    "DoS": [45, 30, 20, 10],
    "Fuzzy": [20, 15, 10, 5],
    "Spoofing": [25, 20, 15, 10],
})
fig2 = px.bar(
    component_data,
    x="Component",
    y=["DoS", "Fuzzy", "Spoofing"],
    labels={"value": "Frequency", "variable": "Attack Type"},
    title="Distribution of Attack Types Across Car Components",
    barmode="stack"
)
st.plotly_chart(fig2)
st.write(
    "This stacked bar chart highlights the distribution of attack types across key automotive components. The engine "
    "is the most frequent target for cyber-attacks."
)