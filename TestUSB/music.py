# sudo apt-get install mpg123
# import mpg321 https://commandmasters.com/commands/mpg321-common/
from animationColors import animatedLights
from threading import Thread
from sense_hat import SenseHat
import os

sense = SenseHat()

# https://forums.raspberrypi.com/viewtopic.php?t=235173
t1 = Thread(target=animatedLights)
threads = [t1]

try: 
    def patMusic():
        print("Pat is on!!!\n")
        os.system("mpg321 PatMethenyGroup_FollowMe_live.mp3")
        os.system("python blynkingMail.py")
    
except KeyboardInterrupt:
    os.clear()

# https://forums.raspberrypi.com/viewtopic.php?t=235173
t2 = Thread(target=patMusic)
threads += [t2]

try: 
    def patMusicOn():
        
        for tloop in threads:
            tloop.join()

except KeyboardInterrupt:
    os.clear()

t1.start()
t2.start()

if __name__ == "__main__":
    result = patMusicOn()
    print("Pat is on!!!\n")