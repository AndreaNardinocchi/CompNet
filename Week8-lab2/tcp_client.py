import socket
from time import sleep
from sense_hat import SenseHat
from env_data import get_environmental_data

deviceID = "device1"
interval = 5

# Create SenseHAT object (used to access temp sensor)
sense = SenseHat()
#UDP Client configuration parameters
serverAddressPort = ("172.236.30.12",41235)

# create a socket object
tcp_socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) 

# bind the socket object to the port
tcp_socket.connect(serverAddressPort)
while True:
    msgFromClient = get_environmental_data(deviceID)
    bytesToSend = str(msgFromClient).encode()
    tcp_socket.sendall(bytesToSend)
    print(f"Sent to server {msgFromClient}")
    sleep(interval)
