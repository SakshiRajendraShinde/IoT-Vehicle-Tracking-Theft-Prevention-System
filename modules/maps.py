import streamlit as st
import folium
from streamlit_folium import st_folium


def show_map(df):

    st.title("🗺️ Fleet Tracking Map")

    if df.empty:

        st.warning(
            "No vehicle data available."
        )

        return

    # =====================================
    # AREA FILTER
    # =====================================

    areas = ["All Areas"] + sorted(
        df["area"].dropna().unique().tolist()
    )

    selected_area = st.selectbox(
        "📍 Filter by Area",
        areas
    )

    if selected_area != "All Areas":

        df = df[
            df["area"] == selected_area
        ]

    if len(df) == 0:

        st.warning(
            "No vehicles found in selected area."
        )

        return

    # =====================================
    # MAP CENTER
    # =====================================

    center_lat = df["latitude"].mean()
    center_lon = df["longitude"].mean()

    fleet_map = folium.Map(
        location=[
            center_lat,
            center_lon
        ],
        zoom_start=7
    )

    # =====================================
    # GEOFENCE CIRCLE
    # =====================================

    folium.Circle(
        location=[18.5204, 73.8567],
        radius=10000,  # 10 km
        popup="Authorized Zone",
        tooltip="Geofence Area",
        fill=True
    ).add_to(fleet_map)

    # =====================================
    # VEHICLE MARKERS
    # =====================================

    for _, row in df.iterrows():

        status = str(
            row["status"]
        ).lower()

        if status == "moving":

            color = "green"

        elif status == "idle":

            color = "orange"

        else:

            color = "red"

        popup_text = f"""
        <b>Vehicle:</b> {row['vehicleNo']}<br>
        <b>Driver:</b> {row['driver']}<br>
        <b>Area:</b> {row['area']}<br>
        <b>Status:</b> {row['status']}<br>
        <b>Speed:</b> {row['speed']} km/h<br>
        <b>Fuel:</b> {row['fuel']} %<br>
        <b>Battery:</b> {row['battery']} %
        """

        folium.Marker(
            location=[
                row["latitude"],
                row["longitude"]
            ],
            popup=popup_text,
            tooltip=row["vehicleNo"],
            icon=folium.Icon(
                color=color,
                icon="car",
                prefix="fa"
            )
        ).add_to(fleet_map)

    # =====================================
    # DISPLAY MAP
    # =====================================

    st_folium(
        fleet_map,
        width=1200,
        height=650
    )

    st.divider()

    # =====================================
    # VEHICLE LOCATION TABLE
    # =====================================

    st.subheader(
        "📋 Vehicle Location Details"
    )

    columns = [
        "vehicleId",
        "vehicleNo",
        "driver",
        "area",
        "latitude",
        "longitude",
        "status",
        "destination"
    ]

    available_columns = [
        col
        for col in columns
        if col in df.columns
    ]

    st.dataframe(
        df[available_columns],
        use_container_width=True
    )