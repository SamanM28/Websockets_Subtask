import socket

IP_ADDRESS = "192.168.4.1"
PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP_ADDRESS, PORT))

while True:
    data = client.recv(1024).decode()
    print("Received data: ", data)

client.close()
