import streamlit as st
import pandas as pd
import os

DATA_FILE = "data/vehicles.csv"


def save_data(df):

    os.makedirs("data", exist_ok=True)

    df.to_csv(
        DATA_FILE,
        index=False
    )


def vehicle_management(df):

    st.title("🚘 Vehicle Management")

    tab1, tab2, tab3 = st.tabs(
        [
            "➕ Add Vehicle",
            "✏️ Edit Vehicle",
            "🗑️ Delete Vehicle"
        ]
    )

    # =====================================
    # ADD VEHICLE
    # =====================================

    with tab1:

        st.subheader(
            "Add New Vehicle"
        )

        with st.form(
            "add_vehicle_form"
        ):

            vehicle_id = st.text_input(
                "Vehicle ID",
                placeholder="VH001"
            )

            vehicle_no = st.text_input(
                "Vehicle Number",
                placeholder="MH14AB1234"
            )

            driver = st.text_input(
                "Driver Name"
            )

            area = st.selectbox(
                "Area",
                [
                    "Pune",
                    "Mumbai",
                    "Nashik",
                    "Nagpur",
                    "Aurangabad",
                    "Other"
                ]
            )

            destination = st.text_input(
                "Destination"
            )

            latitude = st.number_input(
                "Latitude",
                value=18.5204,
                format="%.6f"
            )

            longitude = st.number_input(
                "Longitude",
                value=73.8567,
                format="%.6f"
            )

            speed = st.number_input(
                "Speed (km/h)",
                min_value=0,
                max_value=200,
                value=0
            )

            fuel = st.slider(
                "Fuel %",
                0,
                100,
                80
            )

            battery = st.slider(
                "Battery %",
                0,
                100,
                90
            )

            temperature = st.slider(
                "Engine Temperature",
                0,
                150,
                60
            )

            status = st.selectbox(
                "Status",
                [
                    "Moving",
                    "Idle",
                    "Offline"
                ]
            )

            submit = st.form_submit_button(
                "Add Vehicle"
            )

            if submit:

                new_vehicle = pd.DataFrame([
                    {
                        "vehicleId": vehicle_id,
                        "vehicleNo": vehicle_no,
                        "driver": driver,
                        "area": area,
                        "speed": speed,
                        "fuel": fuel,
                        "battery": battery,
                        "temperature": temperature,
                        "status": status,
                        "destination": destination,
                        "latitude": latitude,
                        "longitude": longitude
                    }
                ])

                updated_df = pd.concat(
                    [df, new_vehicle],
                    ignore_index=True
                )

                save_data(
                    updated_df
                )

                st.success(
                    "Vehicle Added Successfully"
                )

                st.rerun()

    # =====================================
    # EDIT VEHICLE
    # =====================================

    with tab2:

        st.subheader(
            "Edit Vehicle"
        )

        if len(df) == 0:

            st.warning(
                "No vehicles available."
            )

        else:

            selected_vehicle = st.selectbox(
                "Select Vehicle",
                df["vehicleNo"].tolist()
            )

            row = df[
                df["vehicleNo"]
                == selected_vehicle
            ].iloc[0]

            speed = st.number_input(
                "Speed",
                0,
                200,
                int(row["speed"])
            )

            fuel = st.slider(
                "Fuel %",
                0,
                100,
                int(row["fuel"])
            )

            battery = st.slider(
                "Battery %",
                0,
                100,
                int(row["battery"])
            )

            temperature = st.slider(
                "Temperature",
                0,
                150,
                int(row["temperature"])
            )

            status = st.selectbox(
                "Status",
                [
                    "Moving",
                    "Idle",
                    "Offline"
                ],
                index=[
                    "Moving",
                    "Idle",
                    "Offline"
                ].index(
                    row["status"]
                )
            )

            if st.button(
                "Update Vehicle"
            ):

                idx = df[
                    df["vehicleNo"]
                    == selected_vehicle
                ].index[0]

                df.loc[idx, "speed"] = speed
                df.loc[idx, "fuel"] = fuel
                df.loc[idx, "battery"] = battery
                df.loc[idx, "temperature"] = temperature
                df.loc[idx, "status"] = status

                save_data(df)

                st.success(
                    "Vehicle Updated"
                )

                st.rerun()

    # =====================================
    # DELETE VEHICLE
    # =====================================

    with tab3:

        st.subheader(
            "Delete Vehicle"
        )

        if len(df) == 0:

            st.warning(
                "No vehicles available."
            )

        else:

            delete_vehicle = st.selectbox(
                "Vehicle To Delete",
                df["vehicleNo"].tolist(),
                key="delete_vehicle"
            )

            if st.button(
                "Delete Vehicle"
            ):

                df = df[
                    df["vehicleNo"]
                    != delete_vehicle
                ]

                save_data(df)

                st.success(
                    "Vehicle Deleted"
                )

                st.rerun()

    # =====================================
    # CURRENT FLEET
    # =====================================

    st.divider()

    st.subheader(
        "📋 Current Fleet"
    )

    if len(df):

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No vehicles available."
        )