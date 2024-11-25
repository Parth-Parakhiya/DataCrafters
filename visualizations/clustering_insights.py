import streamlit as st
import pandas as pd
from sklearn.cluster import DBSCAN
import plotly.express as px
import pymysql

def load_data():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='car_security'
    )
    data = pd.read_sql("SELECT * FROM dos", conn)
    conn.close()
    return data

st.title("Clustering Insights")

data = load_data()
features = data[['DLC', 'DATA[0]', 'DATA[1]', 'DATA[2]']].fillna(0)

dbscan = DBSCAN(eps=0.5, min_samples=5).fit(features)
data['Cluster'] = dbscan.labels_

fig = px.scatter(data, x='timestamp', y='DLC', color='Cluster', title="DBSCAN Clustering of Attacks")
st.plotly_chart(fig)
