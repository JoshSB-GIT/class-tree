from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP

message = MIMEMultipart('plain')
message['from'] = 'learningmachine119@gmail.com'
message['to'] = 'sierrajoseph8023@gmail.com'
message['subject'] = 'prueba xd'
smtp = SMTP('smtp.gmail.com')
smtp.starttls()