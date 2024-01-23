import smtplib

email = "YOU-MAIL"

receiver_email = input("RECEIVER EMAIL: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(email, "YOU-PASSWORD")

print("SENDING...")
 
server.sendmail(email, receiver_email, text)

print("THE EMAIL HAS BEEN SENT TO" + receiver_email)