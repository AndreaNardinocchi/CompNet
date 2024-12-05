import BlynkLib
from time import sleep
from sense_hat import SenseHat
from capture_image_usb import captureImagePath
from upload_image import upload_image

# initiate SenseHat
sense = SenseHat()
sense.clear()

# Blynk authentication token
BLYNK_AUTH = 'bNfDoU1l_1iSHEIBZrzzGdpa_VtC6rhv'
# Initialize the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)


IMAGE_PATH="./images/sensehat_image.jpg"


blynk.log_event('email_sent')
sense.clear(255,255,255)
captureImagePath(IMAGE_PATH)
result = print(f'Email sent off to your mum with picture {upload_image(IMAGE_PATH)}, and now you got yourself in trouble...') #upload_image(IMAGE_PATH)
blynk.set_property(1,"urls",result) 
sleep(1) # This makes the countdown work

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    
    try:
        while True:
            blynk.run() # Process Blynk events
            sleep(2)  # Add a short delay to avoid high CPU usage

    except KeyboardInterrupt:
        print("Blynk application stopped.")

