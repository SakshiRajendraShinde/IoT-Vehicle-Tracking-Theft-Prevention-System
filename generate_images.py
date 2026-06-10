import pandas as pd
import plotly.express as px
import os

# Create images folder
os.makedirs("images", exist_ok=True)

# Load data
df = pd.read_csv("data/vehicles.csv")

# =====================================
# Area Wise Vehicles
# =====================================

area_df = (
    df.groupby("area")
    .size()
    .reset_index(name="Vehicles")
)

fig = px.bar(
    area_df,
    x="area",
    y="Vehicles",
    color="Vehicles",
    title="Area Wise Vehicle Analysis"
)

fig.write_image(
    "images/area_analysis.png",
    width=1400,
    height=800
)

# =====================================
# Vehicle Status
# =====================================

status_df = (
    df["status"]
    .value_counts()
    .reset_index()
)

status_df.columns = [
    "Status",
    "Count"
]

fig = px.pie(
    status_df,
    names="Status",
    values="Count",
    hole=0.5,
    title="Vehicle Status Distribution"
)

fig.write_image(
    "images/status_analysis.png",
    width=1400,
    height=800
)

# =====================================
# Fuel Analysis
# =====================================

fig = px.bar(
    df,
    x="vehicleNo",
    y="fuel",
    color="fuel",
    title="Fuel Analysis"
)

fig.write_image(
    "images/fuel_analysis.png",
    width=1400,
    height=800
)

# =====================================
# Battery Analysis
# =====================================

fig = px.bar(
    df,
    x="vehicleNo",
    y="battery",
    color="battery",
    title="Battery Analysis"
)

fig.write_image(
    "images/battery_analysis.png",
    width=1400,
    height=800
)

# =====================================
# Speed Analysis
# =====================================

fig = px.line(
    df,
    x="vehicleNo",
    y="speed",
    markers=True,
    title="Speed Monitoring"
)

fig.write_image(
    "images/speed_analysis.png",
    width=1400,
    height=800
)

# =====================================
# Temperature Analysis
# =====================================

fig = px.bar(
    df,
    x="vehicleNo",
    y="temperature",
    color="temperature",
    title="Engine Temperature Analysis"
)

fig.write_image(
    "images/temperature_analysis.png",
    width=1400,
    height=800
)

print("All graph images generated successfully.")