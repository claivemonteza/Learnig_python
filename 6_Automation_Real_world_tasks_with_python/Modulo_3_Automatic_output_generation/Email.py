from email.message import EmailMessage
from Email_Attachments import attachment
import os.path



message = EmailMessage()
sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)


script_dir = os.path.dirname(os.path.abspath(__file__))
attachment_path = os.path.join(script_dir, "attachment.png")
attachment_filename = os.path.basename(attachment_path)
mime_type, mime_subtype = attachment(attachment_path)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachment_filename)


print(message)

