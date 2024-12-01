from sense_hat import SenseHat
sense = SenseHat()

def display_temp_humidity():
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    print(f"Temp: {temperature}C, Hum: {humidity}%")
    
display_temp_humidity()
