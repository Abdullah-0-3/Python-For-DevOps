# First You need to run this command
# python -m smtpd -c DebuggingServer -n localhost:1025

import os
import smtplib

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")

with smtplib.SMTP("localhost", 1025) as smtp:

    subject = "Grab dinner this weekend?"
    body = "How about dinner at 6pm this Saturday?"

    msg = f"Subject: {subject}\n\n{body}"

    SENDER = EMAIL_ADDRESS
    smtp.sendmail(EMAIL_ADDRESS, SENDER, msg)
