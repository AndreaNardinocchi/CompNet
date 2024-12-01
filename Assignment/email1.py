#!/usr/bin/env python
import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime

# Account Information
to = 'oviajantepelomundo76@gmail.com' # Email to send to.
gmail_user = 'andrea.nardinocchi76@gmail.com' # Email to send from. (MUST BE GMAIL)
gmail_password = 'estamos1976' # Gmail password.
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server
today = datetime.date.today()  # Get current time/date

myip=str(subprocess.check_output(['hostname', '-i']))
systemname=str(subprocess.check_output(['hostname', '-f']))

# Creates the text, subject, 'from', and 'to' of the message.
msg = MIMEText(myip + "\n")
msg['Subject'] = 'IPs for ' + systemname + ' on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
# Sends the message
smtpserver.sendmail(gmail_user, [to], msg.as_string())
# Closes the smtp server.
smtpserver.quit()