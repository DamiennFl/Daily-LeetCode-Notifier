import smtplib
from email.message import EmailMessage

textfile = "daily_question.txt"

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# you == the recipient's email address
you = "SENSITIVE INFO"
msg["To"] = you

# Send the message via Gmail's SMTP server.
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Gmail SMTP port

# smtp_username is your smtp server you are sending from. In my case, it is my gmail.
smtp_username = "SENSITIVE INFO"


# DO NOT MAKE THIS PUBLIC... SECRET
smtp_password = "SENSITIVE INFO"  # This is from gmail settings. Note that security settings must be disabled to request an smtp server passcode.


# FYI flagging a message as deleted in a folder different than spam or trash archives the message.
# So to delete the message after sending it through SMTP, I connect to send folder, then move the message to the trash,
# flag it as deleted, and then close the folder. –

try:
    s = smtplib.SMTP(smtp_server, smtp_port)
    s.starttls()  # Secure the connection
    s.login(smtp_username, smtp_password)
    s.send_message(msg)
    s.quit()
    print("Email sent successfully!")
except Exception as e:
    print("An error occurred:", e)
