import time
from simulator import get_acc_z
from location import get_current_location
from storage import add_pothole

THRESHOLD = 2.5
previous_z = 0.0

def detect():
    global previous_z

    current_z = get_acc_z()
    jerk = abs(current_z - previous_z)

    if jerk > THRESHOLD:
        lat, lon = get_current_location()
        event = {
            "time": time.strftime("%H:%M:%S"),
            "jerk": round(jerk, 2),
            "lat": lat,
            "lon": lon
        }
        add_pothole(event)
        print("🚨 POTHOLE DETECTED:", event)

    previous_z = current_z
