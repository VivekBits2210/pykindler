from os import path


def get_smtp_session():
    import smtplib

    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.starttls()

    return session


def login_to_session(session, sender_address):
    session.login(sender_address, get_password(sender_address))


def get_password(sender_address):
    import keyring
    from getpass import getpass

    password = keyring.get_password("system", sender_address)
    if password is None:
        password = getpass(prompt="Enter e-mail password: ")
        keyring.set_password("system", sender_address, password)
    return password


def construct_message(sender_address, receiver_address):
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    message = MIMEMultipart()
    message["From"] = sender_address
    message["To"] = receiver_address
    message["Subject"] = "Book"
    message.attach(MIMEText("", "plain"))
    return message


def attach_file_to_message(message, abs_attachment_path):
    from email.mime.application import MIMEApplication

    filename = path.basename(abs_attachment_path)
    with open(abs_attachment_path, "rb") as file_reader:
        part = MIMEApplication(file_reader.read(), Name=filename)
        part["Content-Disposition"] = f'attachment; filename="{filename}"'
        message.attach(part)
    return message


def send_mail(session, sender_address, receiver_address, message):
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    # session.quit() #TODO: Quit session when it's called, not here
    print("Mail Sent")
    return session
