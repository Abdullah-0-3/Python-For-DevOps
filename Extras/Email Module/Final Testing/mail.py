import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv(os.path.join('D:\Works\Alnafi\DevOps\Python For DevOps\TWS - 18 to 22 Masterclass aka Python For DevOps Github\Email Module', '.env'))
EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

msg = EmailMessage()
msg["Subject"] = "Portfolio"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS

msg.set_content("How about dinner at 6pm this Saturday?")

with open("intro.html", "r") as file:
    file_data = file.read()
    msg.add_alternative(file_data, subtype='html')

with open("Muhammad Abdullah Abrar - DevOps Engineer.pdf", "rb") as file:
    file_data = file.read()
    file_name = "Muhammad Abdullah Abrar - DevOps Engineer.pdf"
    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)