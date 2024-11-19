from sense_hat import SenseHat
sense = SenseHat()


def display_temp_humidity(show_temp=True, show_humidity=True):
# Parameters 'show_temp' and 'show_humidity' control what to display

    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    if show_temp:
        print(f"Temp: {temperature}C")
    if show_humidity:
        print(f"Humidity: {humidity}%")

display_temp_humidity(show_temp=True, show_humidity=False) # Only shows temperature
