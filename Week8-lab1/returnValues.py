from sense_hat import SenseHat
sense = SenseHat()

def get_temp_in_fahrenheit():
    temperature_c = sense.get_temperature()
    temperature_f = (temperature_c * 9/5) + 32
    return temperature_f

temp_f = get_temp_in_fahrenheit()
print(f"Temp: {temp_f}F")
