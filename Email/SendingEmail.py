#! /usr/bin/env python3
#simple mail transfer protcol
import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587) #email service domain name and port number see book for common email providers

conn.ehlo() #connect to the server

conn.starttls() #start tls encryption for sending our pw

conn.login('username', 'password') #login w/ username and pw Note: google has app specific passwords that you may have to configure

conn.sendmail("fromThisEmailAddress@gmail.com", "toThisEmailAddress@gmail.com", 'Subject: This is the subjec \n\n Email content starts here')
# first two params sent from, and send to
#use the two newline characters to serpareate headers from the body
#gmail may have a cap on how many emails you can send like 100-15- at a time or something

conn.quit() #disconnects stmtp protocol
