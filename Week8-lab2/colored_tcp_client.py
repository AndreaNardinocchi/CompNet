import socket
import time
from time import sleep
from sense_hat import SenseHat
from env_data import get_environmental_data

deviceID = "device1"
interval = 5

# Create SenseHAT object (used to access temp sensor)
sense = SenseHat()
sense.clear()
green = (0, 255, 0)
red = (255,0,0)
neutral = ()

# Initial state
is_green = True
sense.clear(red)  # Start with green

#UDP Client configuration parameters
serverAddressPort = ("172.236.30.12",41235)

# create a socket object
tcp_socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) 

# bind the socket object to the port
tcp_socket.connect(serverAddressPort)
while True:
    if is_green:
        sense.clear(green)
        msgFromClient = get_environmental_data(deviceID)
        sense.clear(red)
        
        time.sleep(0.1)

        bytesToSend = str(msgFromClient).encode()
        tcp_socket.sendall(bytesToSend)
        print(f"Sent to server {msgFromClient}")
        sleep(interval)
    else:
        sense.clear(neutral)
        is_red = not is_red
        
        time.sleep(0.1)  # Slight delay to avoid high CPU usage