#! /usr/bin/env python

'''
Send a gmail using python

Pass optional subject and message, a la
	python py_sendmail.py 'my subject' 'my body'


One time steps:
- Configure your username and password 
- Make sure gmail account allows 'less secure app' access

AS2016
'''

import smtplib
import sys

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()

fromd    = 'example@gmail.com' # your email
tod      = fromd               # recipient[s]
username = 'example'           # your email | username
password = 'mypassword'        # your password

# Message
inp = sys.argv[0:]

if len(inp) == 3:
    SUBJECT = inp[1]
    TEXT    = inp[2]
elif len(inp) == 2:
    SUBJECT = inp[1]
    TEXT    = inp[1]
else:
    SUBJECT = 'Computations complete!'
    TEXT    = SUBJECT


TO = tod if type(tod) is list else [tod]

# Construct the email
message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (fromd, ", ".join(TO), SUBJECT, TEXT) 

server.login(username,password)
server.sendmail(fromd, TO, message)
server.quit()