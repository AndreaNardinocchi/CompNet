from sense_hat import SenseHat
import time

GREEN = (0, 255, 0)  # RGB for green
RED = (255, 0, 0)    # RGB for red

# Initialise Sense HAT
sense = SenseHat()
sense.clear(GREEN)  # Start with green color

# Initial state
is_green = True
sense.clear(GREEN)  # Start with green

# Define threshold for shake detection
SHAKE_THRESHOLD = 1.5  # Adjust as needed for sensitivity

def is_shaken():
    # Get raw accelerometer data
    shaken=False
    accel = sense.get_accelerometer_raw()
    x = abs(accel['x'])
    y = abs(accel['y'])
    z = abs(accel['z'])
    
    if x > SHAKE_THRESHOLD or y > SHAKE_THRESHOLD or z > SHAKE_THRESHOLD:
        shaken=True
    # Check if the acceleration exceeds the shake threshold on any axis
    return shaken


while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action, "Trump won!")
        if event.action == "pressed":
            if is_green:
                sense.clear(RED)
                if is_shaken():
                    print("Shakey shakey, #MAGA")
                    sense.clear(RED)  # Set LEDs to red
                    time.sleep(1)  # Keep red for a second
                    sense.clear(GREEN)  # Reset back to green
            
        else:
            sense.clear(GREEN)
        
            time.sleep(0.1)  # Slight delay to avoid high CPU usage


 
