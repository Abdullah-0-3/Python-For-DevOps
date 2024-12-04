import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

msg = EmailMessage()
msg["Subject"] = "Grab dinner this weekend?"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "abdulrehman52427@gmail.com"

msg.set_content("How about dinner at 6pm this Saturday?")

files = ['wolf.jpg', 'wolfy.jpg']

for file in files:
    with open(file, 'rb') as file:
        file_data = file.read()
        file_type = imghdr.what(file.name)

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file.name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)