import time
import threading
from detector import detect
from wifi_check import is_connected_to_toll_gate, toggle_wifi
from uploader import save_to_toll_gate

running = True
stop_program = False
gate_counter = 0
wifi_previous = False

def input_listener():
    global running, stop_program
    while True:
        cmd = input().lower()

        if cmd == "":
            running = not running
            print("🚗 DRIVING" if running else "⛔ PAUSED")

        elif cmd == "w":
            toggle_wifi()

        elif cmd == "q":
            stop_program = True
            break

threading.Thread(target=input_listener, daemon=True).start()

print("SYSTEM STARTED")
print("ENTER → Pause / Resume driving")
print("w + ENTER → Connect WiFi (Toll Gate)")
print("q + ENTER → Quit\n")

try:
    while not stop_program:

        if running:
            detect()

        wifi_current = is_connected_to_toll_gate()

        # Upload ONLY on WiFi connect
        if wifi_current and not wifi_previous:
            save_to_toll_gate(gate_counter)
            gate_counter += 1

        wifi_previous = wifi_current
        time.sleep(1)

except KeyboardInterrupt:
    print("\n🔴 Program interrupted by user")

finally:
    print("✅ System stopped safely")
