import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.example.com'
sender_email = 'your_email@example.com'
receiver_email = 'recipient@example.com'
password = 'your_password'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Sample Email Subject'

body = 'This is a sample email message.'
message.attach(MIMEText(body, 'plain'))

with smtplib.SMTP(smtp_server, 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
