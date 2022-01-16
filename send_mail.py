import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Create a function send()
def send(filename):
    # Declare variables.
    from_email = "sender-email@gmail.com"
    to_email = "recipient-email@gmail.com"
    subject = "💰 [Finance Stock Report]"

    # Create a message object.
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    body = "<b>Hello [Recipient's name]</b> 👋<br>This is your daily Yahoo Finance stock report. Please find attached the <b>.csv file</b> containing your detailed report.<br><br>Best regards,<br><b>The Yahoo Finance Bot</b> 🤖"
    message.attach(MIMEText(body, "html"))

    # Read attachment and send it.
    csv_file = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload((csv_file).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename= " + filename)
    message.attach(part)

    # Convert to a string.
    full_message = message.as_string()

    # First we create an object.
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, "your-app-password")

    server.sendmail(from_email, to_email, full_message)

    # Close the server connection
    server.quit()
