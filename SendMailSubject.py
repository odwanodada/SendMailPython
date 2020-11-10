import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'odwanodada22@gmail.com'
receiver_email = 'lelethundidi@gmail.com'
password = input("Please enter your password: ")
subject = "Hello"
msg = MIMEMultipart()
msg['From']=sender_email
msg['To']=receiver_email
msg['Subject']=subject
body = "Hi ndim uOdwa \n"
body = body + "How was your morning?"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
s.login(sender_email, password)

s.sendmail(sender_email,receiver_email, text)

s.quit()