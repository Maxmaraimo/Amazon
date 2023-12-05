import smtplib
import os
from email.mime.text import MIMEText


def send_email(recipient, subject, body):
    message = MIMEText(body, 'plain')
    message['From'] = 'davlatbemmiya@gmail.com'
    message['To'] = recipient
    message['Subject'] = subject

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('davlatbemmiya@gmail.com', 'davlat88')
        server.sendmail('davlatbemmiya@gmail.com', recipient, message.as_string())


def main():
    recipient = input("Enter recipient's email: ")
    subject = input("Enter email subject: ")
    message = input("Enter email body: ")

    send_email(recipient, subject, message)  # Send the email using the captured details
    print("Email sent successfully!")


if __name__ == "__main__":
    main()
