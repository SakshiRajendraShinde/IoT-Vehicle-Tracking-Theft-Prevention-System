import streamlit as st
import pandas as pd


def show_dashboard(df):

    st.title("📊 Fleet Dashboard")

    if df.empty:

        st.warning(
            "No vehicle data available."
        )

        return

    # ==========================================
    # KPI CALCULATIONS
    # ==========================================

    total_vehicles = len(df)

    active_vehicles = len(
        df[df["status"] == "Moving"]
    )

    idle_vehicles = len(
        df[df["status"] == "Idle"]
    )

    offline_vehicles = len(
        df[df["status"] == "Offline"]
    )

    avg_fuel = round(
        df["fuel"].mean(),
        2
    )

    avg_battery = round(
        df["battery"].mean(),
        2
    )

    alerts = len(
        df[
            (df["fuel"] < 20)
            |
            (df["battery"] < 20)
            |
            (df["temperature"] > 90)
            |
            (df["speed"] > 80)
        ]
    )

    # ==========================================
    # KPI CARDS
    # ==========================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🚗 Total Vehicles",
            total_vehicles
        )

    with col2:

        st.metric(
            "🟢 Active Vehicles",
            active_vehicles
        )

    with col3:

        st.metric(
            "🟡 Idle Vehicles",
            idle_vehicles
        )

    col4, col5, col6 = st.columns(3)

    with col4:

        st.metric(
            "🔴 Offline Vehicles",
            offline_vehicles
        )

    with col5:

        st.metric(
            "⛽ Avg Fuel",
            f"{avg_fuel}%"
        )

    with col6:

        st.metric(
            "⚠️ Alerts",
            alerts
        )

    st.divider()

    # ==========================================
    # VEHICLE STATUS SUMMARY
    # ==========================================

    st.subheader(
        "🚘 Fleet Status Summary"
    )

    status_counts = (
        df["status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = [
        "Status",
        "Count"
    ]

    st.dataframe(
        status_counts,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # VEHICLE OVERVIEW TABLE
    # ==========================================

    st.subheader(
        "📋 Vehicle Overview"
    )

    display_cols = [

        "vehicleId",
        "vehicleNo",
        "driver",
        "area",
        "speed",
        "fuel",
        "battery",
        "temperature",
        "status",
        "destination"

    ]

    available_cols = [

        col
        for col in display_cols
        if col in df.columns

    ]

    st.dataframe(
        df[available_cols],
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # QUICK INSIGHTS
    # ==========================================

    st.subheader(
        "📈 Dashboard Insights"
    )

    highest_speed = df.loc[
        df["speed"].idxmax()
    ]

    lowest_fuel = df.loc[
        df["fuel"].idxmin()
    ]

    highest_temp = df.loc[
        df["temperature"].idxmax()
    ]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            f"🏎 Fastest Vehicle: "
            f"{highest_speed['vehicleNo']} "
            f"({highest_speed['speed']} km/h)"
        )

    with col2:

        st.warning(
            f"⛽ Lowest Fuel: "
            f"{lowest_fuel['vehicleNo']} "
            f"({lowest_fuel['fuel']}%)"
        )

    with col3:

        st.error(
            f"🌡 Highest Temperature: "
            f"{highest_temp['vehicleNo']} "
            f"({highest_temp['temperature']}°C)"
        )