# import BlynkLib
#from threading import Thread
from sense_hat import SenseHat

import time
import pyttsx3
#from beatingHeart import beatHeartNow
#from animationColors import animatedLights
# from blynk_email_function import blynkEmailMum
# from capture_image import capture_image
# from upload_image import upload_image

# https://forums.raspberrypi.com/viewtopic.php?t=235173
#t1 = Thread(target=animatedLights)
#threads = [t1]
#t2 = Thread(target=patMusic)
#threads += [t2]
#t3 = Thread(target=blynkEmailMum)
#threads += [t3]

# One time initialization
engine = pyttsx3.init()

# Set properties _before_ you add things to say
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

sense = SenseHat()

# Z = beatHeartNow()
R = (200, 0, 0)
B = (0, 127, 255)
G = (0, 200, 0)
X = (0, 0, 0)
W = (255,255,255)

#sense.clear(Z)



def countdownOne():

    for i in range(15, -1, -1):
        if i>12 :
           sense.clear(B)
        elif i > 9 :
           sense.clear(R)
           #animatedLights()
           #time.sleep(0.1)
        elif i >= 4 :
            text = R
            bg = W
            sense.show_letter(str(i), text, bg)
        else:
            text = G
            bg = X
            sense.show_letter(str(i), text, bg)
        time.sleep(1)


    for i in range(12, -1, -1):
        if i>5:
            sense.show_message("BOOM!!!!", scroll_speed=0.03, text_colour=[255, 255, 255])
            bg = X 
            # Queue up things to say.
            # There will be a short break between each one
            # when spoken, like a pause between sentences.
            engine.say("BOOM Shut that freaking thing down, and get the hell out of here Now")
            # Flush the say() queue and play the audio
            engine.runAndWait()
            # Program will not continue execution until
            # all speech is done talking
            time.sleep(0.7) 
        elif i<=0:
            #t1.start()
            #t2.start()
            
            #t3.start()
            time.sleep(0.1) 
            for i in range(350, -1, -1):
                if i > 5:
                    sense.clear(255,255,255)
                    from music import patMusicOn
                    patMusicOn()
                    time.sleep(0.1) 
                else:
                    #blynkEmailMum()
                    sense.clear(255,255,255)


            
        
   # for tloop in threads:
    #    tloop.join()
        # beatHeartNow() & patMusic() 
        
    
    

# if __name__ == "__main__":
  #  countdownOne()
   # countdownTwo()
    # print("CountdownSpeak is on!!")


   # for i in range(12, -1, -1):
    #    if i>5:



  

sense.clear()
    