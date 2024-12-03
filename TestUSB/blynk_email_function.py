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

def blynkEmailMum():
    
   # for i in range(350, -1, -1):
    #    if i>0:
     #       sense.clear()
      #  elif i <= 0:
    blynk.log_event('email_sent')
    sense.clear(255,255,255)
    captureImagePath(IMAGE_PATH)
    result = upload_image(IMAGE_PATH)
    blynk.set_property(1,"urls",result) 
sleep(1) # This makes the countdown work

# blynkEmailMum()



# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print('Email sent off to your mum, and now you have got yourself in trouble...')
    try:
        while True:
            blynk.run() # Process Blynk events
            sleep(2)  # Add a short delay to avoid high CPU usage

    except KeyboardInterrupt:
        print("Blynk application stopped.")

