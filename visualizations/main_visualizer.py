import streamlit as st
import pandas as pd
import numpy as np
import pymysql
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from keras.models import Model, Sequential
from keras.layers import Dense, Input
import plotly.express as px
import plotly.graph_objects as go
import smtplib
from email.mime.text import MIMEText
import requests
import io

# Database connection
def load_data(table_name):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='car_security'
    )
    query = f"SELECT * FROM {table_name}"
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Mock API fetch for real-time data
def fetch_real_time_data():
    url = "https://mockapi.com/car-hacking"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(io.StringIO(response.text))
    else:
        st.warning("Unable to fetch real-time data. Using static dataset.")
        return None

# Send anomaly alert email
def send_email_alert(subject, body):
    sender = "alert@carsecurity.com"
    receiver = "admin@carsecurity.com"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, "your_email_password")
        server.sendmail(sender, receiver, msg.as_string())

# Sidebar for dataset and visualization selection
st.sidebar.header("Controls")
data_source = st.sidebar.selectbox(
    "Choose Data Source",
    ["DoS", "Fuzzy", "Gear", "RPM", "Real-Time Data"]
)
visualization_type = st.sidebar.selectbox(
    "Choose Visualization",
    [
        "Attack Type Overview",
        "Trend Analysis (Animated)",
        "Combined Insights",
        "Clustering & Anomalies",
        "Historical vs Current Comparison"
    ]
)

# Load dataset
if data_source == "Real-Time Data":
    data = fetch_real_time_data()
    if data is None:
        data = load_data("dos")
else:
    data = load_data(data_source.lower())

# Preprocess data
if "timestamp" in data.columns:
    data["timestamp"] = pd.to_datetime(data["timestamp"])

# Feature selection for clustering and anomalies
features = data[["DLC", "DATA[0]", "DATA[1]", "DATA[2]"]].fillna(0)

# Visualization logic
if visualization_type == "Attack Type Overview":
    st.header("Attack Type Overview")
    flag_counts = data["flag"].value_counts()
    pie_fig = px.pie(names=flag_counts.index, values=flag_counts.values, title="Attack Type Distribution")
    st.plotly_chart(pie_fig)

    bar_fig = px.bar(x=flag_counts.index, y=flag_counts.values, labels={"x": "Attack Type", "y": "Frequency"})
    st.plotly_chart(bar_fig)

elif visualization_type == "Trend Analysis (Animated)":
    st.header("Trend Analysis")
    trend_fig = px.line(data, x="timestamp", y="DLC", color="flag", animation_frame="timestamp",
                        title="Animated Trend of Attack Types Over Time")
    st.plotly_chart(trend_fig)

elif visualization_type == "Combined Insights":
    st.header("Combined Insights")
    correlation = data.corr()
    heatmap_fig = px.imshow(correlation, title="Correlation Heatmap")
    st.plotly_chart(heatmap_fig)

    flag_counts = data["flag"].value_counts()
    bar_fig = px.bar(x=flag_counts.index, y=flag_counts.values, labels={"x": "Attack Type", "y": "Frequency"})
    st.plotly_chart(bar_fig)

elif visualization_type == "Clustering & Anomalies":
    st.header("Clustering & Anomalies")

    # k-means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    data["Cluster"] = kmeans.fit_predict(features)
    cluster_fig = px.scatter(data, x="timestamp", y="DLC", color="Cluster", title="K-means Clustering")
    st.plotly_chart(cluster_fig)

    # Isolation Forest for anomalies
    iso_forest = IsolationForest(contamination=0.02)
    data["Anomaly"] = iso_forest.fit_predict(features)
    anomaly_data = data[data["Anomaly"] == -1]
    if len(anomaly_data) > 0:
        send_email_alert("Anomaly Detected!", f"{len(anomaly_data)} anomalies were detected.")
    anomaly_fig = px.scatter(anomaly_data, x="timestamp", y="DLC", color="flag", title="Anomalies Detected")
    st.plotly_chart(anomaly_fig)

elif visualization_type == "Historical vs Current Comparison":
    st.header("Historical vs Current Comparison")
    historical_data = load_data("dos")  # Load historical data as a baseline
    comparison_fig = px.line(
        historical_data,
        x="timestamp",
        y="DLC",
        title="Historical vs Current Comparison"
    )
    st.plotly_chart(comparison_fig)

# Download raw data
if st.sidebar.button("Download Data"):
    csv = data.to_csv(index=False)
    st.download_button("Download Current Data", csv, file_name=f"{data_source}_data.csv", mime="text/csv")

# Display raw data if selected
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)
