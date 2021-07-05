from os import path
import smtplib


def send_a_bunch_of_files_to_kindle(file_list, from_file, to_file):
    for abs_file_path in file_list:
        if not is_file_attachable(abs_file_path):
            print(f"Attachment too big: Skipping {abs_file_path}..")
            continue

        GmailKindleClient(from_file, to_file, abs_file_path).send_email_with_book()


def is_file_attachable(self):
    from ..constants import gmail_attachment_threshold_mb

    file_size_in_mb = path.getsize(self.abs_attachment_path) / 1e6
    return file_size_in_mb < self.abs_attachment_path - 2


class GmailKindleClient:
    def __init__(self, sender, receiver, abs_attachment_path=""):
        self.session = smtplib.SMTP("smtp.gmail.com", 587)
        self.session.starttls()
        self.sender = sender
        self.receiver = receiver
        self.abs_attachment_path = abs_attachment_path
        self.message = self.construct_empty_message()

    def send_email_with_book(self):
        self.login_to_session()
        self.attach_file_to_message()
        self.send_mail()
        self.session.quit()

    def login_to_session(self):
        from smtplib import SMTPAuthenticationError
        from keyring import delete_password
        from keyring.errors import PasswordDeleteError

        try:
            self.session.login(self.sender, self.get_password())
            return True
        except SMTPAuthenticationError:
            try:
                print("Invalid credentials, deleting from keyring....")
                delete_password("system", self.sender)
            except PasswordDeleteError:
                print("ERROR: Keyring corrupted!")
        return False

    def get_password(self):
        import keyring
        from getpass import getpass

        password = keyring.get_password("system", self.sender)
        if password is None:
            password = getpass(prompt="Enter e-mail password: ")
            keyring.set_password("system", self.sender, password)
        return password

    def construct_empty_message(self):
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        message = MIMEMultipart()
        message["From"] = self.sender
        message["To"] = self.receiver
        message["Subject"] = "Book"
        message.attach(MIMEText("", "plain"))
        return message

    def attach_file_to_message(self):
        from email.mime.application import MIMEApplication

        filename = path.basename(self.abs_attachment_path)
        with open(self.abs_attachment_path, "rb") as file_reader:
            part = MIMEApplication(file_reader.read(), Name=filename)
            part["Content-Disposition"] = f'attachment; filename="{filename}"'
            self.message.attach(part)

    def send_mail(self):
        text = self.message.as_string()
        self.session.sendmail(self.sender, self.receiver, text)
        print("Mail Sent")
