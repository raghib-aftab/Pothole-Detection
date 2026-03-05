wifi_connected = False

def toggle_wifi():
    global wifi_connected
    wifi_connected = not wifi_connected
    print("📡 WiFi CONNECTED" if wifi_connected else "📴 WiFi DISCONNECTED")

def disconnect_wifi():
    global wifi_connected
    wifi_connected = False
    print("📴 WiFi AUTO-DISCONNECTED after upload")

def is_connected_to_toll_gate():
    return wifi_connected
