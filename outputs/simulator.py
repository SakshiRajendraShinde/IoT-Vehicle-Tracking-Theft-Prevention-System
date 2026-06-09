import random
import time
import csv
from datetime import datetime
from math import radians, sin, cos, sqrt, atan2

SAFE_LAT = 19.9975
SAFE_LON = 73.7898

GEOFENCE_RADIUS = 500

CSV_FILE = "vehicle_logs.csv"


def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371000

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def generate_coordinates():

    lat = SAFE_LAT + random.uniform(-0.01, 0.01)
    lon = SAFE_LON + random.uniform(-0.01, 0.01)

    return lat, lon


def check_geofence(lat, lon):

    distance = calculate_distance(
        SAFE_LAT,
        SAFE_LON,
        lat,
        lon
    )

    return distance > GEOFENCE_RADIUS


def generate_google_maps(lat, lon):

    return f"https://maps.google.com/?q={lat},{lon}"


def log_data(timestamp, lat, lon, status, alert):

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            lat,
            lon,
            status,
            alert
        ])


def run_tracking():

    print("Vehicle Tracking Started...")

    while True:

        lat, lon = generate_coordinates()

        theft = check_geofence(lat, lon)

        status = "MOVING"

        alert = "NONE"

        if theft:
            alert = "THEFT ALERT"

        timestamp = datetime.now()

        maps_link = generate_google_maps(
            lat,
            lon
        )

        print("\n======================")
        print("Time:", timestamp)
        print("Latitude:", lat)
        print("Longitude:", lon)
        print("Maps:", maps_link)
        print("Alert:", alert)

        log_data(
            timestamp,
            lat,
            lon,
            status,
            alert
        )

        time.sleep(5)


if __name__ == "__main__":
    run_tracking()