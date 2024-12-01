from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
green = (0, 255, 0)
red = (255,0,0)
blue = (0, 0, 255)
while True:
  temp = sense.get_temperature()
  if temp >=25:
    sense.show_message("HOT!", text_colour = red)
  elif temp >15:
    sense.show_message("Cool!", text_colour = blue)
  else:
    sense.show_message("Cold!!!!", text_colour = green)
  print(temp)
