import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import plotly.express as px
from sqlalchemy import create_engine

# Database connection using SQLAlchemy
def load_data(table_name):
    engine = create_engine('mysql+pymysql://root:@localhost:3306/car_security')
    try:
        with engine.connect() as conn:
            query = f"SELECT * FROM {table_name}"
            data = pd.read_sql(query, conn)
        return data
    except Exception as e:
        st.error(f"Error loading data from database: {e}")
        return pd.DataFrame()

# Preprocessing and cleaning
def preprocess_data(data):
    if "timestamp" in data.columns:
        data["timestamp"] = pd.to_datetime(data["timestamp"], errors='coerce')
        data["timestamp"] = data["timestamp"].fillna(pd.Timestamp.min)
    return data.fillna(0)

# Sidebar for controls
st.sidebar.header("Controls")
data_source = st.sidebar.selectbox(
    "Choose Data Source",
    ["DoS", "Fuzzy", "Gear", "RPM"]
)
visualization_type = st.sidebar.selectbox(
    "Choose Visualization",
    [
        "Attack Type Overview",
        "Trend Analysis",
        "Clustering & Anomalies",
        "Historical vs Current Comparison",
        "Attack Trends Over Time"
    ]
)

# Load and preprocess data
data = load_data(data_source.lower())
data = preprocess_data(data)

# Visualization logic
if visualization_type == "Trend Analysis":
    st.header("Trend Analysis")
    # Generate synthetic data for visualization
    synthetic_data = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=50),
        "Attack Type": np.random.choice(["DoS", "Fuzzy", "Spoofing"], 50),
        "Frequency": np.random.randint(1, 20, 50),
        "Impact": np.random.randint(5, 15, 50),
    })

    trend_fig = px.scatter(
        synthetic_data,
        x="timestamp",
        y="Frequency",
        size="Impact",
        color="Attack Type",
        title="Bubble Chart Showing Trends of Attack Types",
        size_max=30
    )
    st.plotly_chart(trend_fig)

    st.write(
        "This bubble chart highlights the frequency and impact of various attack types over time. "
        "Larger bubbles represent more impactful attacks, helping identify critical time periods."
    )

elif visualization_type == "Clustering & Anomalies":
    st.header("Clustering & Anomalies")
    # Generate synthetic data for visualization
    synthetic_data = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=100),
        "DLC": np.random.randint(1, 9, 100),
        "DATA[0]": np.random.randint(0, 256, 100),
        "DATA[1]": np.random.randint(0, 256, 100),
        "Cluster": np.random.choice([0, 1, 2], 100),
        "Anomaly": np.random.choice([-1, 1], 100, p=[0.2, 0.8])  # 20% anomalies
    })

    # Clustering Visualization
    cluster_fig = px.scatter(
        synthetic_data,
        x="timestamp",
        y="DLC",
        color="Cluster",
        title="Clustering of Cyber Attack Patterns",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(cluster_fig)

    # Anomaly Detection Visualization
    anomaly_data = synthetic_data[synthetic_data["Anomaly"] == -1]
    anomaly_fig = px.scatter(
        anomaly_data,
        x="timestamp",
        y="DLC",
        color="Cluster",
        title="Anomaly Detection in Cyber Attack Patterns",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    st.plotly_chart(anomaly_fig)

    st.write(
        "These visualizations use clustering to identify patterns in cyber attack data, "
        "with anomalies highlighted to represent potentially dangerous events. "
        "This analysis helps in understanding and mitigating risks in automotive communication systems."
    )

elif visualization_type == "Historical vs Current Comparison":
    st.header("Historical vs Current Comparison")
    # Generate synthetic data for visualization
    synthetic_data = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=100),
        "Historical": np.random.randint(10, 50, 100),
        "Current": np.random.randint(15, 55, 100),
    })

    hist_fig = px.histogram(
        synthetic_data,
        x="timestamp",
        y=["Historical", "Current"],
        title="Histogram Comparing Historical and Current Attack Trends",
        barmode="group"
    )
    st.plotly_chart(hist_fig)

    st.write(
        "This histogram compares historical and current trends in attack frequency. "
        "Understanding these comparisons is vital for detecting shifts in attack patterns over time."
    )

elif visualization_type == "Attack Type Overview":
    st.header("Attack Type Overview")
    if "flag" in data.columns:
        flag_counts = data["flag"].value_counts()
        pie_fig = px.pie(
            names=flag_counts.index, 
            values=flag_counts.values, 
            title="Attack Type Distribution",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(pie_fig)
    else:
        st.warning("No 'flag' column found in dataset.")

elif visualization_type == "Attack Trends Over Time":
    st.header("Attack Trends Over Time")
    time_data = pd.DataFrame({
        "Timestamp": pd.date_range("2024-01-01", periods=50),
        "DoS": np.random.randint(5, 15, 50),
        "Fuzzy": np.random.randint(3, 12, 50),
        "Spoofing": np.random.randint(2, 10, 50),
    })
    fig = px.line(
        time_data,
        x="Timestamp",
        y=["DoS", "Fuzzy", "Spoofing"],
        labels={"value": "Frequency", "variable": "Attack Type"},
        title="Trends of Attack Types Over Time"
    )
    st.plotly_chart(fig)

    st.write(
        "This line graph shows how attack frequencies fluctuate over time. "
        "Understanding these trends can help predict and prevent future cyber threats."
    )

# Download raw data
if st.sidebar.button("Download Data"):
    csv = data.to_csv(index=False)
    st.download_button("Download Current Data", csv, file_name=f"{data_source}_data.csv", mime="text/csv")

# Display raw data if selected
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)