import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


def show_prediction(df):

    st.title("🔮 AI Fleet Prediction Engine")

    if df.empty:

        st.warning(
            "No vehicle data available."
        )

        return

    # ==========================================
    # CURRENT FLEET STATISTICS
    # ==========================================

    total_vehicles = len(df)

    active_vehicles = len(
        df[df["status"] == "Moving"]
    )

    inactive_vehicles = len(
        df[df["status"] == "Offline"]
    )

    idle_vehicles = len(
        df[df["status"] == "Idle"]
    )

    st.subheader("📊 Current Fleet Snapshot")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🚗 Total Vehicles",
        total_vehicles
    )

    c2.metric(
        "🟢 Active",
        active_vehicles
    )

    c3.metric(
        "🟡 Idle",
        idle_vehicles
    )

    c4.metric(
        "🔴 Offline",
        inactive_vehicles
    )

    st.divider()

    # ==========================================
    # VEHICLE POPULATION FORECAST
    # ==========================================

    st.subheader(
        "📈 Vehicle Population Prediction"
    )

    months = [
        "Current",
        "Month 1",
        "Month 2",
        "Month 3",
        "Month 4",
        "Month 5",
        "Month 6"
    ]

    growth_rate = 0.08

    prediction_values = []

    current = total_vehicles

    for _ in range(len(months)):

        prediction_values.append(
            round(current)
        )

        current = current * (
            1 + growth_rate
        )

    population_df = pd.DataFrame(
        {
            "Month": months,
            "Vehicles": prediction_values
        }
    )

    fig_population = px.line(
        population_df,
        x="Month",
        y="Vehicles",
        markers=True,
        title="Fleet Growth Forecast"
    )

    st.plotly_chart(
        fig_population,
        use_container_width=True
    )

    # ==========================================
    # POPULATION CHANGE ANALYSIS
    # ==========================================

    change = (
        prediction_values[-1]
        - prediction_values[0]
    )

    if change > 0:

        st.success(
            f"📈 Predicted Increase: +{change} vehicles in next 6 months"
        )

    elif change < 0:

        st.error(
            f"📉 Predicted Decrease: {change} vehicles"
        )

    else:

        st.info(
            "No major change predicted."
        )

    st.divider()

    # ==========================================
    # AREA-WISE FORECAST
    # ==========================================

    st.subheader(
        "🗺️ Area-wise Vehicle Forecast"
    )

    area_df = (
        df.groupby("area")
        .size()
        .reset_index(name="Current Vehicles")
    )

    area_df["Predicted Vehicles"] = (
        area_df["Current Vehicles"]
        * 1.15
    ).round()

    fig_area = px.bar(
        area_df,
        x="area",
        y=[
            "Current Vehicles",
            "Predicted Vehicles"
        ],
        barmode="group",
        title="Area Population Forecast"
    )

    st.plotly_chart(
        fig_area,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # ACTIVE VS INACTIVE FORECAST
    # ==========================================

    st.subheader(
        "🚦 Active Vehicle Prediction"
    )

    prediction_status = pd.DataFrame(
        {
            "Category": [
                "Active",
                "Inactive"
            ],
            "Current": [
                active_vehicles,
                inactive_vehicles
            ],
            "Predicted": [
                round(active_vehicles * 1.10),
                max(
                    round(inactive_vehicles * 0.90),
                    0
                )
            ]
        }
    )

    fig_status = px.bar(
        prediction_status,
        x="Category",
        y=[
            "Current",
            "Predicted"
        ],
        barmode="group",
        title="Vehicle Activity Forecast"
    )

    st.plotly_chart(
        fig_status,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # FUEL TREND FORECAST
    # ==========================================

    st.subheader(
        "⛽ Fuel Consumption Forecast"
    )

    avg_fuel = df["fuel"].mean()

    fuel_months = [
        "Current",
        "M1",
        "M2",
        "M3",
        "M4",
        "M5",
        "M6"
    ]

    fuel_values = []

    current_fuel = avg_fuel

    for _ in range(len(fuel_months)):

        fuel_values.append(
            round(current_fuel, 2)
        )

        current_fuel -= 2

    fuel_df = pd.DataFrame(
        {
            "Month": fuel_months,
            "Fuel": fuel_values
        }
    )

    fig_fuel = px.area(
        fuel_df,
        x="Month",
        y="Fuel",
        title="Fuel Trend Forecast"
    )

    st.plotly_chart(
        fig_fuel,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # MAINTENANCE PREDICTION
    # ==========================================

    st.subheader(
        "🔧 Maintenance Prediction"
    )

    maintenance_df = df.copy()

    maintenance_df[
        "Maintenance Risk"
    ] = np.where(

        (
            maintenance_df["battery"] < 30
        )
        |
        (
            maintenance_df["temperature"] > 90
        ),

        "High",

        "Low"
    )

    risk_count = (
        maintenance_df[
            "Maintenance Risk"
        ]
        .value_counts()
        .reset_index()
    )

    risk_count.columns = [
        "Risk",
        "Count"
    ]

    fig_risk = px.pie(
        risk_count,
        names="Risk",
        values="Count",
        hole=0.5,
        title="Maintenance Risk Analysis"
    )

    st.plotly_chart(
        fig_risk,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # PREDICTION TABLE
    # ==========================================

    st.subheader(
        "📋 Vehicle Prediction Summary"
    )

    display_columns = [
        "vehicleId",
        "vehicleNo",
        "area",
        "fuel",
        "battery",
        "temperature",
        "status"
    ]

    available_columns = [
        col
        for col in display_columns
        if col in maintenance_df.columns
    ]

    st.dataframe(
        maintenance_df[
            available_columns +
            ["Maintenance Risk"]
        ],
        use_container_width=True
    )