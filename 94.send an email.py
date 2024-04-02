import smtplib # simple mail transfer protocol library

sender = "sender@gmail.com"
receiver = "receiver@gmail.com "
password = "password"
subject = "Python email test"
body = " I am sending this email using python code"

# header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in....")
    server.sendmail(sender,receiver,message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
