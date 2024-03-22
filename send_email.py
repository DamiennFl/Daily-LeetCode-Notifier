import smtplib
from email.message import EmailMessage

textfile = 'testmessage.txt'

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
me = 'damien.flutre@gmail.com'
you = 'damien.flutre@gmail.com'
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = me
msg['To'] = you

# Send the message via Gmail's SMTP server.
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Gmail SMTP port
smtp_username = 'damien.flutre@gmail.com'
smtp_password = 'hmqx pfrs xbfs nexk'  # Use app-specific password if 2FA enabled

try:
    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()  # Secure the connection
    s.login(smtp_username, smtp_password)
    s.send_message(msg)
    s.quit()
    print("Email sent successfully!")
except Exception as e:
    print("An error occurred:", e)
