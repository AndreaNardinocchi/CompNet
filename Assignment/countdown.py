from sense_hat import SenseHat
import time

sense = SenseHat()

R = (200, 0, 0)
G = (0, 200, 0)
X = (0, 0, 0)
W = (255,255,255)

for i in range(15, -1, -1):
    if i > 9 :
      sense.clear(R)
      
    elif i >= 4:
        text = R
        bg = W
        sense.show_letter(str(i), text, bg)
        
    elif i < 4 :
        text = G
        bg = X
        sense.show_letter(str(i), text, bg)
    time.sleep(1)
    
while True:        
    sense.show_message("BOOM", scroll_speed=0.03, text_colour=[255, 255, 255])
    bg = X 
    time.sleep(1)
    
    sense.clear()