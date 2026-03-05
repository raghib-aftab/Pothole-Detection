import json
import os
import math
from storage import get_buffer, clear_buffer
from location import get_current_location
from wifi_check import disconnect_wifi

DB_FOLDER = "pothole_db"
os.makedirs(DB_FOLDER, exist_ok=True)

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return round(2 * R * math.asin(math.sqrt(a)), 2)

def save_to_toll_gate(gate_index):
    data = get_buffer()
    if not data:
        return

    gate_lat, gate_lon = get_current_location()

    for p in data:
        p["distance_to_toll_gate_km"] = calculate_distance(
            p["lat"], p["lon"], gate_lat, gate_lon
        )

    gate_name = f"Toll_Gate_{chr(65 + gate_index)}"
    path = f"{DB_FOLDER}/{gate_name}.json"

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    clear_buffer()
    print(f"✅ Data saved to {gate_name}")

    # Auto disconnect after upload
    disconnect_wifi()
