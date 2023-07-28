#!/usr/bin/env python3

from email.message import EmailMessage
from getpass import getpass
from smtplib import SMTP_SSL
from sys import exit
import ssl


smtp_server = 'smtp.com'
smtp_port = 587
username = 'mail.com'
password = getpass('Enter your email account password: ')

sender = 'mail.com'
destination = 'mail.com'
subject = 'Sent from Python 3.x'
content = 'Hello! This was sent to you via Python 3.x!'

# Create a text/plain message
msg = EmailMessage()
# import pdb;pdb.set_trace()
# msg.set_content(content)

msg['Subject'] = subject
msg['From'] = sender
msg['To'] = destination

import pdb;
pdb.set_trace()

try:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    s = SMTP_SSL(smtp_server, smtp_port, context=context)
    s.login(username, password)
    try:
        s.send_message(msg)
    finally:
        s.quit()

except Exception as E:
    exit('Mail failed: {}'.format(str(E)))
