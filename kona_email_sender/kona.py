from email.message import EmailMessage
from password import password
import ssl 
import smtplib

email_sender = 'soheliarefinkona@gmail.com'
email_password = password

email_receiver = 'samiajannat6789@gmail.com'

subject = 'Sending email to me just to let me know that Im learning Python.'
body = """
Wohoo, You've successfully learnt how to send emails via Python. Learning Python is fun.

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())