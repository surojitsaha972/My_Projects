from email.message import EmailMessage
import ssl
import smtplib

sender = "karmakarsouvik297@gmail.com"
pas = "gyyiuucmgceqmqof"

receiver = "mrsouvikkarmakar3@gmail.com"
sub = "Subject"
body = "Hello"

em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['subject'] = sub
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
    smtp.login(sender,pas)
    smtp.sendmail(sender, receiver, em.as_string())

# import smtplib
# import ssl

# # Setup port number and servr name

# smtp_port = 587                 # Standard secure SMTP port
# smtp_server = "smtp.gmail.com"  # Google SMTP Server

# email_from = "karmakarsouvik297@gmail.com"
# email_to = "souvikk329@gmail.com"

# pswd = "gyyiuucmgceqmqof"

# # content of message

# message = "Hello everyone"

# # Create context
# simple_email_context = ssl.create_default_context()


# try:
#     # Connect to the server
#     print("Connecting to server...")
#     TIE_server = smtplib.SMTP(smtp_server, smtp_port)
#     TIE_server.starttls(context=simple_email_context)
#     TIE_server.login(email_from, pswd)
#     print("Connected to server :-)")
    
#     # Send the actual email
#     print()
#     print(f"Sending email to - {email_to}")
#     TIE_server.sendmail(email_from, email_to, message)
#     print(f"Email successfully sent to - {email_to}")

# # If there's an error, print it out
# except Exception as e:
#     print(e)

# # Close the port
# finally:
#     TIE_server.quit()

# from multiprocessing import connection
# import smtplib
# # from sqlite3 import connect

# sender = "karmakarsouvik297@gmail.com"
# pas = "gyyiuucmgceqmqof"
# rec = "souvikk329@gmail.com"

# connect = smtplib.SMTP("smtp.gmail.com")
# connect.starttls()
# connect.login(user = sender, password = pas)

# content = "Subject: Eta holo SUB \n\n Hello"
# # connect.sendmail()
# try:
#     connect.sendmail(from_addr = sender, to_addrs = rec, msg = content)
# except Exception as e:
#     print(e)
# connect.close()

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# def send_email(sender_email, sender_password, recipient_email, subject, body):
#     # Set up the email content
#     message = MIMEMultipart()
#     message['From'] = sender_email
#     message['To'] = recipient_email
#     message['Subject'] = subject
#     message.attach(MIMEText(body, 'plain'))

#     # Connect to the SMTP server and send the email
#     try:
#         smtp_server = 'smtp.gmail.com'
#         smtp_port = 587  # Replace with the appropriate port number
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.starttls()
#             server.login(sender_email, sender_password)
#             server.sendmail(sender_email, recipient_email, message.as_string())
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"An error occurred while sending the email: {e}")

# # Replace the placeholders with your own email details
# sender_email = 'karmakarsouvik297@gmail.com'
# sender_password = 'gyyiuucmgceqmqof'
# recipient_email = 'souvikk329@gmail.com'
# subject = 'Test Email'
# body = 'This is a test email sent from Python.'

# send_email(sender_email, sender_password, recipient_email, subject, body)

# import smtplib

# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)

# # start TLS for security
# s.starttls()
# send1 = "mrsouvikkarmakar3@gmail.com"
# pas1 = "Viraterfansouvikami18"
# send2 = "karmakarsouvik297@gmail.com"
# pas2 = "gyyiuucmgceqmqof"
# # Authentication
# # s.login("karmakarsouvik297@gmail.com", "gyyiuucmgceqmqof")
# s.login(send2, pas2)

# # message to be sent
# message = "Message_you_need_to_send"

# # sending the mail
# s.sendmail(send2, send1, message)

# # terminating the session
# s.quit()