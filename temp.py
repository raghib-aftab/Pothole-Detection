import socket
import time

UDP_IP = ""
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("📡 Connected to ESP32 WiFi")
print("🚧 Pothole Detection Data")
print("-" * 50)

while True:
    data, addr = sock.recvfrom(1024)
    print(time.strftime("%H:%M:%S"), "->", data.decode())