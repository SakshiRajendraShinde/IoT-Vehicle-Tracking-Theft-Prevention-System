import streamlit as st
import pandas as pd
import os
from datetime import datetime
from fpdf import FPDF


REPORT_FOLDER = "reports"

os.makedirs(
    REPORT_FOLDER,
    exist_ok=True
)


# ==========================================
# PDF GENERATOR
# ==========================================

def generate_pdf(df):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        "B",
        16
    )

    pdf.cell(
        200,
        10,
        "Smart Fleet SaaS Report",
        ln=True,
        align="C"
    )

    pdf.ln(5)

    pdf.set_font(
        "Arial",
        "",
        11
    )

    pdf.cell(
        200,
        10,
        f"Generated: {datetime.now()}",
        ln=True
    )

    pdf.ln(5)

    total = len(df)

    active = len(
        df[df["status"] == "Moving"]
    )

    idle = len(
        df[df["status"] == "Idle"]
    )

    offline = len(
        df[df["status"] == "Offline"]
    )

    avg_fuel = round(
        df["fuel"].mean(),
        2
    )

    pdf.cell(
        200,
        10,
        f"Total Vehicles: {total}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Active Vehicles: {active}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Idle Vehicles: {idle}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Offline Vehicles: {offline}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Average Fuel: {avg_fuel}%",
        ln=True
    )

    pdf.ln(10)

    pdf.set_font(
        "Arial",
        "B",
        12
    )

    pdf.cell(
        40,
        10,
        "Vehicle"
    )

    pdf.cell(
        30,
        10,
        "Area"
    )

    pdf.cell(
        25,
        10,
        "Speed"
    )

    pdf.cell(
        25,
        10,
        "Fuel"
    )

    pdf.cell(
        30,
        10,
        "Status",
        ln=True
    )

    pdf.set_font(
        "Arial",
        "",
        10
    )

    for _, row in df.iterrows():

        pdf.cell(
            40,
            10,
            str(row["vehicleNo"])
        )

        pdf.cell(
            30,
            10,
            str(row["area"])
        )

        pdf.cell(
            25,
            10,
            str(row["speed"])
        )

        pdf.cell(
            25,
            10,
            str(row["fuel"])
        )

        pdf.cell(
            30,
            10,
            str(row["status"]),
            ln=True
        )

    pdf_path = os.path.join(
        REPORT_FOLDER,
        "fleet_report.pdf"
    )

    pdf.output(pdf_path)

    return pdf_path


# ==========================================
# REPORT PAGE
# ==========================================

def show_reports(df):

    st.title("📑 Fleet Reports Center")

    if df.empty:

        st.warning(
            "No data available."
        )

        return

    # ==========================================
    # REPORT SUMMARY
    # ==========================================

    st.subheader(
        "📊 Fleet Summary"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Vehicles",
        len(df)
    )

    c2.metric(
        "Avg Fuel",
        f"{round(df['fuel'].mean(),2)}%"
    )

    c3.metric(
        "Avg Battery",
        f"{round(df['battery'].mean(),2)}%"
    )

    c4.metric(
        "Avg Speed",
        f"{round(df['speed'].mean(),2)} km/h"
    )

    st.divider()

    # ==========================================
    # DAILY REPORT
    # ==========================================

    st.subheader(
        "📅 Daily Report"
    )

    daily_report = pd.DataFrame(
        {
            "Metric": [
                "Total Vehicles",
                "Moving",
                "Idle",
                "Offline"
            ],
            "Value": [
                len(df),
                len(df[df["status"] == "Moving"]),
                len(df[df["status"] == "Idle"]),
                len(df[df["status"] == "Offline"])
            ]
        }
    )

    st.dataframe(
        daily_report,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # VEHICLE DATA
    # ==========================================

    st.subheader(
        "🚗 Vehicle Report"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # CSV EXPORT
    # ==========================================

    st.subheader(
        "📥 Export CSV"
    )

    csv = df.to_csv(
        index=False
    )

    st.download_button(
        label="Download CSV Report",
        data=csv,
        file_name="fleet_report.csv",
        mime="text/csv"
    )

    st.divider()

    # ==========================================
    # PDF EXPORT
    # ==========================================

    st.subheader(
        "📄 Generate PDF Report"
    )

    if st.button(
        "Generate PDF"
    ):

        pdf_path = generate_pdf(df)

        with open(
            pdf_path,
            "rb"
        ) as pdf_file:

            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name="fleet_report.pdf",
                mime="application/pdf"
            )

        st.success(
            "PDF Generated Successfully"
        )

    st.divider()

    # ==========================================
    # AREA-WISE REPORT
    # ==========================================

    st.subheader(
        "📍 Area-wise Vehicle Report"
    )

    area_report = (
        df.groupby("area")
        .size()
        .reset_index(
            name="Vehicle Count"
        )
    )

    st.dataframe(
        area_report,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # ALERT REPORT
    # ==========================================

    st.subheader(
        "🚨 Alert Candidates"
    )

    alerts = df[
        (df["fuel"] < 20)
        |
        (df["battery"] < 20)
        |
        (df["temperature"] > 90)
        |
        (df["speed"] > 80)
    ]

    if len(alerts):

        st.dataframe(
            alerts,
            use_container_width=True
        )

    else:

        st.success(
            "No alert candidates found."
        )