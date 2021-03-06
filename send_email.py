# importing dependencies(all of them are in-built)
from smtplib import *
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

# using Object-Oriented Programming to create non-cloud drafts and just send them when you want to do so


class send_email:
    # Getting all input variables and making them available for the whole class
    def __init__(self, user, to, subject, body, path=None, filename=None, msg=None):
        self.user = user
        self.to = to
        self.subject = subject
        self.body = body
        self.msg = msg
        status = "Not Drafted"
        self.status = status
        if path is not None:
            self.path = path
            self.filename = filename

    # Option to draft the email in advance if it is to be sent in a hurry

    def create_draft(self):
        # Creating the instance of MIMEMultipart to format the email
        data = MIMEMultipart()
        data["From"] = self.user
        data["Subject"] = self.subject
        data.attach(MIMEText((self.body), "plain"))

        # Adding the attachment if a path is given
        try:
            if (self.path) is not None:
                attachment = open((self.path), "rb")
                p = MIMEBase("application", "octet-stream")
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header(
                    "Content-Disposition", "attachment; filename= %s" % (self.filename)
                )
                data.attach(p)
        except AttributeError:
            pass
        (self.status) = "Drafted"
        (self.msg) = data.as_string()
        if self.status == "Drafted":
            return True
        else:
            return False

    # Creating the email if not already drafted and sending it using smtplib

    def send(self, password):
        # The email creation
        if self.status == "Not Drafted":
            data = MIMEMultipart()
            data["From"] = self.user
            data["Subject"] = self.subject
            data.attach(MIMEText((self.body), "plain"))

            # The attachment part
            try:
                if (self.path) is not None:
                    attachment = open((self.path), "rb")
                    p = MIMEBase("application", "octet-stream")
                    p.set_payload((attachment).read())
                    encoders.encode_base64(p)
                    p.add_header(
                        "Content-Disposition",
                        "attachment; filename= %s" % (self.filename),
                    )
                    data.attach(p)
            except AttributeError:
                pass
            (self.msg) = data.as_string()

        try:
            # Setting up the server
            server = SMTP("smtp.gmail.com", 587)
            server.starttls()
            # Loging in
            server.login((self.user), password)
            (message) = self.msg

            for rec in self.to:
                server.sendmail((self.user), rec, message)

            server.quit()
            return True

        except:
            print("give valid credentials")

# Thanks for using my small attempt towards Object-Oriented Programming
