import smtplib
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
from sense_hat import SenseHat
import time

sense = SenseHat()

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'andrea.nardinocchi76@email.com' #change this to match your gmail account
GMAIL_PASSWORD = 'estamos1976'  #change this to match your gmail password



class Emailer:
    def sendmail(self, recipient, subject, content):

        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

sender = Emailer()

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        if event.action == "pressed":
            sendTo = 'oviajantepelomundo76@gmail.com'
            emailSubject = "Button Press Detected!"
            emailContent = "The button has been pressed at: " + time.ctime()
            sender.sendmail(sendTo, emailSubject, emailContent)
            print("Email Sent")

    time.sleep(0.1)