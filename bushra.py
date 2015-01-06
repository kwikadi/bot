import sendgrid
from datetime import date, timedelta

print date.today() - timedelta(days=7)

sendgrid = sendgrid.SendGridClient(api_user, api_key)
message = sendgrid.Mail()

message.add_to("test@sendgrid.com")
message.set_from("you@youremail.com")
message.set_subject("Weekly Newsletter for IdeaBin")
message.set_html("and easy to do anywhere, even with Python")

sendgrid.send(message)
