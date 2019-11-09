from pymongo import MongoClient
import smtplib, ssl

client = MongoClient('mongodb://localhost:27017')
db = client.techRingdb

def send_mail(col, link):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "virajlakshitha39@gmail.com"
    receiver_email = col["email"]
    password = "pckkotte"
    message = "Hey! Price of "+ col["product"] + " has been decreased. You can check it from " + link + "\t From TechRing"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

def push_notification(id, link):
    for col in db.Notification.find({"pid": id}):
        if col != "":
            send_mail(col, link)

