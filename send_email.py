from email.mime.text import MIMEText
import smtplib
# Import of libraries and classes

def send_email(email, weight, average_weight, count):
# Defintion send_email function
    from_email = "email address you are sending from"
    from_password = "your email password"
    to_email = email
    # Store the from email, its password and the email where the message
    # will be sent

    subject = "Weight data"
    message = "Hey there! Your weight is <strong>%s</strong> and the average\
    is <strong>%s</strong>.<br>That is calculated out <strong>%s</strong> of people</br>" % (weight, average_weight, count)
    # Subject and message of the email that will be sent

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
    #Send the email via STMP servers of gmail
