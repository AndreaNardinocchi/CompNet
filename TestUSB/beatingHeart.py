# https://forums.raspberrypi.com/viewtopic.php?t=319689

from sense_hat import SenseHat
import math
import time

sense = SenseHat()

sense.set_rotation(180)


try:
    def beatHeartNow():
        while True:
            # Define some colours
            n = (0, 0, 0)  # closed
            rsin = ((math.sin(time.time()) + 1) / 2)
            rsin *= 255.0
            rsin = int(rsin)
            r = (rsin, 0, 0)  # colour
            # Set up where each colour will display
            heart = [
            n, n, n, n, n, n, n, n,
            n, r, r, n, n, r, r, n,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            n, r, r, r, r, r, r, n,
            n, n, r, r, r, r, n, n,
            n, n, n, r, r, n, n, n,
            n, n, n, n, n, n, n, n,
        ]
            # Display these colours on the LED matrix
            sense.set_pixels(heart)
            time.sleep(0.0000000001)

except KeyboardInterrupt:
    sense.clear()

if __name__ == "__main__":
    result = beatHeartNow()
    
