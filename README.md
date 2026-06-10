# 🚗 IoT Vehicle Tracking & Theft Prevention System

## 📌 Overview

The **IoT Vehicle Tracking & Theft Prevention System** is a Smart Fleet Management and Vehicle Security Dashboard developed using Python and Streamlit. The project simulates real-world vehicle tracking operations by monitoring vehicle location, movement status, fuel level, battery health, engine temperature, and driver performance.

The system includes geofencing, theft detection alerts, predictive analytics, route monitoring, area-wise fleet analysis, interactive maps, automated reporting, and vehicle management capabilities through a modern SaaS-style dashboard.

This project demonstrates how IoT-based vehicle monitoring solutions are used in logistics companies, delivery services, school transportation systems, and personal vehicle security applications.

---

# 🎯 Problem Statement

Vehicle owners and fleet operators face several challenges:

* Difficulty tracking vehicle locations
* Unauthorized vehicle movement
* Vehicle theft risks
* Lack of centralized monitoring
* Poor fleet utilization visibility
* Fuel and maintenance monitoring issues
* Absence of real-time alerts

This project provides a centralized solution for monitoring and managing vehicles through an intelligent dashboard.

---

# 🚀 Key Features

### 🚗 Vehicle Tracking

* Vehicle monitoring dashboard
* Current vehicle information
* Live location visualization
* Route monitoring

### 📍 Geofencing

* Define authorized operating zones
* Detect vehicles leaving safe areas
* Unauthorized movement alerts

### 🛡️ Theft Prevention

* Theft detection logic
* Geofence breach alerts
* Suspicious movement monitoring
* Security notifications

### ⚠️ Alert System

* Overspeed detection
* Low fuel alerts
* Low battery alerts
* Engine overheating alerts
* Offline vehicle alerts

### ⛽ Fuel Monitoring

* Fuel percentage tracking
* Fuel utilization analysis
* Low fuel detection

### 🔋 Vehicle Health Monitoring

* Battery status
* Engine temperature
* Health scoring
* Maintenance indicators

### 👨‍✈️ Driver Monitoring

* Driver assignment
* Driver safety score
* Driving behavior analysis

### 📊 Analytics Dashboard

* Area-wise fleet analysis
* Vehicle status distribution
* Fuel analytics
* Battery analytics
* Speed monitoring
* Vehicle health analysis

### 🔮 Prediction Engine

* Fleet growth prediction
* Future vehicle estimation
* Area-wise forecasting

### 📄 Report Generation

* CSV export
* PDF report generation
* Fleet summary reports
* Alert reports

### 🌙 SaaS Dashboard Experience

* Dark mode
* Light mode
* Interactive Plotly charts
* Responsive layout
* Modern UI design

---

# 🏭 Industry Relevance

Similar technologies are used by:

* Uber
* Ola
* Rapido
* Logistics Companies
* Fleet Management Providers
* School Bus Tracking Systems
* Truck Monitoring Companies
* Vehicle Security Providers

Business benefits include:

* Reduced theft risk
* Better fleet visibility
* Improved operational efficiency
* Reduced maintenance costs
* Enhanced driver accountability
* Improved customer service

---

# 🛠️ Technology Stack

| Category      | Technology |
| ------------- | ---------- |
| Frontend      | Streamlit  |
| Backend       | Python     |
| Data Handling | Pandas     |
| Visualization | Plotly     |
| Maps          | Folium     |
| Reporting     | FPDF       |
| Prediction    | NumPy      |
| Storage       | CSV        |

---

# 📂 Project Structure

```text
IoT-Vehicle-Tracking-Theft-Prevention-System/

│
├── assets/
│   └── style.css
│
├── data/
│   └── vehicles.csv
│
├── images/
│
├── reports/
│
├── modules/
│   ├── __init__.py
│   ├── dashboard.py
│   ├── vehicle_manager.py
│   ├── fleet_analytics.py
│   ├── maps.py
│   ├── alerts.py
│   ├── prediction.py
│   └── reports.py
│
├── app.py
├── requirements.txt
├── README.md
└── generate_images.py
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/IoT-Vehicle-Tracking-Theft-Prevention-System.git
```

## 2. Move into Project Directory

```bash
cd IoT-Vehicle-Tracking-Theft-Prevention-System
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

# 📊 Dashboard Modules

## Dashboard

Displays:

* Total Vehicles
* Active Vehicles
* Idle Vehicles
* Offline Vehicles
* Average Fuel Level
* Fleet Summary

---

## Vehicle Management

Allows:

* Add Vehicle
* Edit Vehicle
* Delete Vehicle
* Assign Driver
* Update Vehicle Status

---

## Analytics

Provides:

* Area-wise Analysis
* Fuel Monitoring
* Battery Analysis
* Vehicle Health Score
* Driver Safety Score
* Status Distribution

---

## Interactive Map

Displays:

* Vehicle Locations
* Vehicle Status Colors
* Geographical Monitoring

Status Colors:

* 🟢 Moving
* 🟡 Idle
* 🔴 Offline

---

## Alerts

Detects:

* Low Fuel
* Low Battery
* Engine Overheating
* Overspeeding
* Theft Risk

---

## Prediction Engine

Forecasts:

* Future Vehicle Growth
* Fleet Expansion Trends
* Area-wise Vehicle Projection

---

## Reports

Generate:

* Daily Reports
* Fleet Reports
* PDF Reports
* CSV Reports

---

# 📈 Sample Vehicle Data

```json
{
  "vehicleId": "VH001",
  "vehicleNo": "MH14AB1234",
  "driver": "Rahul Patil",
  "speed": 52,
  "fuel": 75,
  "battery": 85,
  "temperature": 72,
  "status": "Moving",
  "area": "Pune",
  "destination": "Mumbai"
}
```

---

# 📷 Screenshots

## Dashboard

Add:

```text
images/dashboard.png
```

## Analytics

Add:

```text
images/analytics.png
```

## Map

Add:

```text
images/map.png
```

## Alerts

Add:

```text
images/alerts.png
```

## Prediction

Add:

```text
images/prediction.png
```

## Reports

Add:

```text
images/reports.png
```

---

# 🎓 Learning Outcomes

Through this project, I learned:

* IoT Fleet Monitoring Concepts
* Vehicle Security Systems
* Geofencing Logic
* Predictive Analytics
* Dashboard Development
* Data Visualization
* Python Application Development
* SaaS Dashboard Design
* Report Automation
* GitHub Project Management

---

# 🔮 Future Enhancements

* ESP32 Integration
* GPS Module Integration
* GSM Alert System
* MQTT Communication
* Real-Time Vehicle Tracking
* Cloud Database Integration
* Mobile Application
* AI-Based Theft Detection
* Driver Behavior Analytics
* Route Optimization

---

# 👨‍💻 Author

Sakshi Shinde

Developed as an IoT and Fleet Management project to demonstrate vehicle tracking, theft prevention, predictive analytics, and dashboard development concepts.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share your feedback

Happy Coding 🚀
