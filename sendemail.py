import smtplib

# fromaddr = '<email>'
# toaddr = '<email>'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""

username = raw_input("Enter Username(your gmail address) to login: ")
password = raw_input("Enter Password: ")

# fromname = 'Me'
# toname = 'you'
fromname = raw_input("Enter Sender Name: ")
fromaddr = raw_input("Enter Sender Email Address: ")
toname = raw_input("Enter Recipient Name: ")
toaddr = raw_input("Enter Recipient Email Address: ")
# subject = 'Hello world.'
# msg = 'this is a test'
subject = raw_input("Enter Subject: ")
msg = raw_input("Enter Message: ")

messagetosend = message.format(
 fromname,
 fromaddr,
 toname,
 toaddr,
 subject,
 msg)

# Credentials (if needed)
# username = '<email>'
# #password = '{youremailapppassword}''
# password = '<pwd>'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()