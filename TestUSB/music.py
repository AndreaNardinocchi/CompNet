# import pywhatkit 

# pywhatkit.playonyt('PMG - Follow Me live - AN')

# sudo apt-get install mpg123

# import mpg321 https://commandmasters.com/commands/mpg321-common/
from animationColors import animatedLights
from threading import Thread
from sense_hat import SenseHat
# from blynk_email_function import blynkEmailMum
import os

sense = SenseHat()
# https://forums.raspberrypi.com/viewtopic.php?t=235173
t1 = Thread(target=animatedLights)
threads = [t1]

#t3 = Thread(target=blynkEmailMum)
#threads += [t3]


try: 
    def patMusic():
        print("Pat is on!!!\n")
        os.system("mpg321 PatMethenyGroup_FollowMe_live.mp3")
        os.system("python blynk_email_function.py")
        # os.clear()
    

except KeyboardInterrupt:
    os.clear()

t2 = Thread(target=patMusic)
threads += [t2]


try: 
    def patMusicOn():
        
        for tloop in threads:
            tloop.join()
    
     #   os.clear()
      #  blynkEmailMum()
            
            #t3.start()
            # 

except KeyboardInterrupt:
    os.clear()



t1.start()
t2.start()
#t3.start()

if __name__ == "__main__":
    result = patMusicOn()
    print("Pat is on!!!\n")
    
    #os.clear()
    #blynkEmailMum()


# scan on
# pair deviceid 04:E8:B9:07:9D:82 ANDREADELL


