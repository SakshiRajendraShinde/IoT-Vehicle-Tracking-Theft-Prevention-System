import streamlit as st
import pandas as pd


# ==========================================
# GEOFENCE SETTINGS
# ==========================================

SAFE_LAT = 18.5204
SAFE_LON = 73.8567
SAFE_RADIUS = 0.10  # approx simulation radius


def check_geofence(lat, lon):

    if abs(lat - SAFE_LAT) > SAFE_RADIUS:
        return False

    if abs(lon - SAFE_LON) > SAFE_RADIUS:
        return False

    return True


# ==========================================
# ALERT PAGE
# ==========================================

def show_alerts(df):

    st.title("🚨 Vehicle Alerts & Theft Detection")

    if df.empty:

        st.warning(
            "No vehicle data available."
        )

        return

    alerts = []

    # ==========================================
    # ALERT ENGINE
    # ==========================================

    for _, row in df.iterrows():

        vehicle = row["vehicleNo"]

        # Low Fuel

        if row["fuel"] < 20:

            alerts.append(
                {
                    "Vehicle": vehicle,
                    "Alert": "⛽ Low Fuel",
                    "Severity": "High"
                }
            )

        # Low Battery

        if row["battery"] < 20:

            alerts.append(
                {
                    "Vehicle": vehicle,
                    "Alert": "🔋 Low Battery",
                    "Severity": "High"
                }
            )

        # Overspeed

        if row["speed"] > 80:

            alerts.append(
                {
                    "Vehicle": vehicle,
                    "Alert": "🏎️ Overspeed Detected",
                    "Severity": "Medium"
                }
            )

        # Temperature

        if row["temperature"] > 90:

            alerts.append(
                {
                    "Vehicle": vehicle,
                    "Alert": "🌡️ Engine Overheating",
                    "Severity": "Critical"
                }
            )

        # Theft Detection

        if (
            row["status"] == "Moving"
            and row["speed"] > 0
            and row["fuel"] < 10
        ):

            alerts.append(
                {
                    "Vehicle": vehicle,
                    "Alert": "🚨 Possible Theft Activity",
                    "Severity": "Critical"
                }
            )

        # Geofence Check

        if (
            "latitude" in row
            and "longitude" in row
        ):

            inside_zone = check_geofence(
                row["latitude"],
                row["longitude"]
            )

            if not inside_zone:

                alerts.append(
                    {
                        "Vehicle": vehicle,
                        "Alert": "📍 Vehicle Outside Geofence",
                        "Severity": "Critical"
                    }
                )

    # ==========================================
    # KPI CARDS
    # ==========================================

    total_alerts = len(alerts)

    critical = len(
        [
            a
            for a in alerts
            if a["Severity"] == "Critical"
        ]
    )

    high = len(
        [
            a
            for a in alerts
            if a["Severity"] == "High"
        ]
    )

    medium = len(
        [
            a
            for a in alerts
            if a["Severity"] == "Medium"
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "⚠️ Total Alerts",
            total_alerts
        )

    with col2:

        st.metric(
            "🔴 Critical",
            critical
        )

    with col3:

        st.metric(
            "🟠 High",
            high
        )

    with col4:

        st.metric(
            "🟡 Medium",
            medium
        )

    st.divider()

    # ==========================================
    # ALERT TABLE
    # ==========================================

    st.subheader(
        "🚨 Active Alerts"
    )

    if len(alerts) == 0:

        st.success(
            "No active alerts detected."
        )

    else:

        alert_df = pd.DataFrame(alerts)

        st.dataframe(
            alert_df,
            use_container_width=True
        )

    st.divider()

    # ==========================================
    # CRITICAL VEHICLES
    # ==========================================

    st.subheader(
        "🔴 Critical Vehicles"
    )

    critical_alerts = [

        alert

        for alert in alerts

        if alert["Severity"] == "Critical"

    ]

    if len(critical_alerts) == 0:

        st.success(
            "No critical vehicles."
        )

    else:

        for alert in critical_alerts:

            st.error(
                f"{alert['Vehicle']} → {alert['Alert']}"
            )

    st.divider()

    # ==========================================
    # ALERT SUMMARY
    # ==========================================

    st.subheader(
        "📊 Alert Summary"
    )

    summary = {
        "Total Vehicles": len(df),
        "Vehicles With Alerts": len(
            set(
                [
                    a["Vehicle"]
                    for a in alerts
                ]
            )
        ),
        "Total Alerts": total_alerts
    }

    st.json(summary)