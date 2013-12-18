# Program to send emails from python
# Written in Python 3.3

import smtplib
import getpass

def send_mail(username, password, serv):
	
	# Asks for the from email address, the to email address and then the
	# messages
	from_email = input('From Email : ')
	to_email = input('To Email : ')
	message = input('Message: ')
	
	# Sends message
	server = smtplib.SMTP(serv)
	server.starttls()
	server.login(username,password)
	server.sendmail(from_email, to_email, message)
	
	#Confirmation message
	print("Sent email to " + to_email)
	server.quit()

if __name__ == "__main__":
	# Asks for username and password
	username = input('Username : ')
	password = getpass.getpass()
	provider = input('Gmail, Outlook, or Hotmail: ')
	provider = provider.strip().lower()
	if provider == 'gmail':
		serv = 'smtp.gmail.com:587'
	elif provider == 'outlook' or provider == 'hotmail':
		serv = 'smtp.live.com:587'
	
	send_mail(username, password, serv)
