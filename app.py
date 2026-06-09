import streamlit as st
import pandas as pd
import os

from modules.dashboard import show_dashboard
from modules.vehicle_manager import vehicle_management
from modules.fleet_analytics import show_analytics
from modules.alerts import show_alerts
from modules.maps import show_map
from modules.prediction import show_prediction
from modules.reports import show_reports

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Smart Fleet SaaS",
    page_icon="🚗",
    layout="wide"
)

# ==================================================
# LOAD CSS
# ==================================================

def load_css():

    css_path = "assets/style.css"

    if os.path.exists(css_path):

        with open(css_path) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ==================================================
# DATA FILE
# ==================================================

DATA_FILE = "data/vehicles.csv"

# ==================================================
# CREATE DATA FILE IF NOT EXISTS
# ==================================================

if not os.path.exists(DATA_FILE):

    os.makedirs("data", exist_ok=True)

    sample_df = pd.DataFrame(
        columns=[
            "vehicleId",
            "vehicleNo",
            "driver",
            "area",
            "speed",
            "fuel",
            "battery",
            "temperature",
            "status",
            "destination",
            "latitude",
            "longitude"
        ]
    )

    sample_df.to_csv(
        DATA_FILE,
        index=False
    )

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(DATA_FILE)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🚗 Smart Fleet SaaS")

theme = st.sidebar.radio(
    "Theme",
    [
        "Dark",
        "Light"
    ]
)

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Vehicle Management",
        "Analytics",
        "Map",
        "Alerts",
        "Prediction",
        "Reports"
    ]
)

# ==================================================
# HEADER
# ==================================================

st.markdown(
    """
    # 🚗 Smart Fleet SaaS

    ### Vehicle Tracking, Theft Prevention & Analytics Platform
    """
)

# ==================================================
# ROUTING
# ==================================================

if menu == "Dashboard":

    show_dashboard(df)

elif menu == "Vehicle Management":

    vehicle_management(df)

elif menu == "Analytics":
    
    show_analytics(df)

elif menu == "Map":

    show_map(df)

elif menu == "Alerts":

    show_alerts(df)

elif menu == "Prediction":

    show_prediction(df)

elif menu == "Reports":

    show_reports(df)