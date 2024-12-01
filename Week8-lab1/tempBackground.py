from sense_hat import SenseHat
sense = SenseHat()

# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

while True:

  # Take readings from all three sensors
  temp = sense.get_temperature()
  pres = sense.get_pressure()
  hum = sense.get_humidity()

  # Round the values to one decimal place
  temp = round(temp, 1)
  pres = round(pres, 1)
  hum = round(hum, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(temp) + " Pressure: " + str(pres) + " Humidity: " + str(hum)
  
  if temp > 20.3 and temp < 26.7:
    bg = green
  elif temp >10 and temp <= 20.3:
    bg = black
  else:
    bg = red
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, back_colour=bg)
