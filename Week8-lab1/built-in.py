# Using built-in functions with SenseHAT
from sense_hat import SenseHat
sense = SenseHat()

temperature = sense.get_temperature()
rounded_temp = round(temperature, 1) # Round to 1 decimal place
print(f"Temp: {rounded_temp}C")
