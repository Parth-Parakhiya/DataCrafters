import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import plotly.express as px
from sqlalchemy import create_engine

def load_data():
    engine = create_engine('postgresql://admin:password@localhost/car_security')
    return pd.read_sql("SELECT * FROM dos", con=engine)

st.title("Anomaly Detection - Isolation Forest")

data = load_data()
data['Timestamp'] = pd.to_datetime(data['Timestamp'], unit='s')

# Isolation Forest for Anomaly Detection
model = IsolationForest(contamination=0.02)
data['Anomaly'] = model.fit_predict(data[['DLC', 'DATA[0]', 'DATA[1]', 'DATA[2]']])

anomaly_data = data[data['Anomaly'] == -1]
fig = px.scatter(anomaly_data, x='Timestamp', y='DLC', color='Flag', title="Detected Anomalies")
st.plotly_chart(fig)

st.subheader("Raw Anomalies Data")
st.write(anomaly_data)
