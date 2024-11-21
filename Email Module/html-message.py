import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

msg = EmailMessage()
msg["Subject"] = "Grab dinner this weekend?"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS

msg.set_content("How about dinner at 6pm this Saturday?")

msg.add_alternative("""\
<!DOCTYPE html>
<style>
    .container {
        padding: 20px;
        background-color: #f9f9f9;
        color: #333;
        font-family: Arial, sans-serif;
    }
    h1 {
        color: #333;
    }
</style>
<html>
    <body>
        <div class="container">
            <h1>Muhammmad Abdullah Abrar</h1>
        </div>
    </body>
</html> 
""", subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)