import smtplib

#https://myaccount.google.com/lesssecureapps ==to make it send email
s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'odwanodada22@gmail.com'
receiver_address = 'odwanodada22@gmail.com'
password = input('Please enter password: ')

s.starttls()
s.login(sender_email_id, password)
message = "Bayageza abazali"
s.sendmail(sender_email_id, receiver_address, message)


s.quit(),