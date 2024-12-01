# Using built-in functions with SenseHAT
from sense_hat import SenseHat
sense = SenseHat()

with open("sensor_data.txt", "w") as file:
    temperature = sense.get_temperature()
    file.write(f"Temperature: {temperature}°C\n")


with open("sensor_data.txt", "a") as file:
    temperature = sense.get_temperature()
    file.write(f"Temperature: {temperature}°C\n")
