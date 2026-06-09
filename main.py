import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Vehicle Tracking Dashboard",
    layout="wide"
)

st.title("🚗 Smart Vehicle Tracking & Theft Prevention System")

df = pd.read_csv("vehicles.csv")

# KPI Cards

total = len(df)
active = len(df[df["status"] == "Moving"])
idle = len(df[df["status"] == "Idle"])
offline = len(df[df["status"] == "Offline"])

avg_fuel = round(df["fuel"].mean(), 2)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("🚗 Total Vehicles", total)
col2.metric("🟢 Active", active)
col3.metric("🟡 Idle", idle)
col4.metric("🔴 Offline", offline)
col5.metric("⛽ Avg Fuel", f"{avg_fuel}%")

st.divider()

# Vehicle Table

st.subheader("Vehicle Information")

st.dataframe(df, use_container_width=True)

st.divider()

# Speed Analytics

st.subheader("Speed Monitoring")

fig_speed = px.bar(
    df,
    x="vehicleNo",
    y="speed",
    color="status",
    title="Vehicle Speed"
)

st.plotly_chart(fig_speed, use_container_width=True)

st.divider()

# Fuel Monitoring

st.subheader("Fuel Monitoring")

fig_fuel = px.bar(
    df,
    x="vehicleNo",
    y="fuel",
    title="Fuel Levels"
)

st.plotly_chart(fig_fuel, use_container_width=True)

st.divider()

# Battery Monitoring

st.subheader("Battery Monitoring")

fig_battery = px.bar(
    df,
    x="vehicleNo",
    y="battery",
    title="Battery Levels"
)

st.plotly_chart(fig_battery, use_container_width=True)

st.divider()

# Vehicle Status Pie Chart

st.subheader("Vehicle Status Distribution")

status_count = df["status"].value_counts()

fig_pie = px.pie(
    values=status_count.values,
    names=status_count.index
)

st.plotly_chart(fig_pie, use_container_width=True)

st.divider()

# Driver Safety Score

st.subheader("Driver Safety Score")

df["safety_score"] = (
    100
    - (df["speed"] * 0.3)
    - ((100 - df["fuel"]) * 0.1)
)

fig_driver = px.bar(
    df,
    x="driver",
    y="safety_score"
)

st.plotly_chart(fig_driver, use_container_width=True)

st.divider()

# Theft Alerts

st.subheader("Security Alerts")

alerts = []

for _, row in df.iterrows():

    if row["fuel"] < 20:
        alerts.append(
            f"⚠️ Low Fuel Alert: {row['vehicleNo']}"
        )

    if row["speed"] > 80:
        alerts.append(
            f"⚠️ Overspeed Alert: {row['vehicleNo']}"
        )

if alerts:

    for alert in alerts:
        st.error(alert)

else:
    st.success("No Active Alerts")

st.divider()

# Fleet Prediction

st.subheader("Fleet Growth Prediction")

days = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

vehicles = np.array(
    [40, 42, 45, 47, 50]
)

model = LinearRegression()

model.fit(days, vehicles)

future_day = np.array([[6]])

prediction = int(
    model.predict(future_day)[0]
)

growth = round(
    ((prediction - 50) / 50) * 100,
    2
)

st.metric(
    "Predicted Vehicles Tomorrow",
    prediction
)

if growth > 0:
    st.success(
        f"Fleet Growth Expected: +{growth}%"
    )
else:
    st.warning(
        f"Fleet Growth Expected: {growth}%"
    )