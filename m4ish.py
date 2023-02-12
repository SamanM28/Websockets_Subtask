import socket
import re
import keyboard

HOST = '192.168.4.1'  # IP address of the ESP8266
PORT = 80  # Port number used by the ESP8266

def parse_data(data):
    # Parse the data received from the ESP8266
    pattern = r'ax: (\d+) ay: (\d+) az: (\d+) gx: (\d+) gy: (\d+) gz: (\d+)'
    match = re.match(pattern, data)
    if match:
        ax, ay, az, gx, gy, gz = [int(match.group(i)) for i in range(1, 7)]
        return ax, ay, az, gx, gy, gz
    return None

def control_keyboard(ax, ay, az, gx, gy, gz):
    # Use the sensor data to control the keyboard
    if ax > 10000:
        keyboard.press('w')
    else:
        keyboard.release('w')
    if ax < -10000:
        keyboard.press('s')
    else:
        keyboard.release('s')
    if gy > 1000:
        keyboard.press('d')
    else:
        keyboard.release('d')
    if gy < -1000:
        keyboard.press('a')
    else:
        keyboard.release('a')

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
sock.bind((HOST, PORT))

# Listen for incoming connections
sock.listen(1)

print('Waiting for a connection...')

# Accept incoming connections
conn, addr = sock.accept()
print('Connected by', addr)

# Receive and parse data from the ESP8266
while True:
    data = conn.recv(1024)
    if not data:
        break
    data = data.decode('utf-8').strip()
    print('Received data:', data)
    sensor_data = parse_data(data)
    if sensor_data:
        ax, ay, az, gx, gy, gz = sensor_data
        control_keyboard(ax, ay, az, gx, gy, gz)

# Close the connection
conn.close()
