#importing dependencies(all of them are in-built)
from smtplib import *
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#using Object-Oriented Programming to create non-cloud drafts and just send them when you want to do so
class send_email:
    #Getting all input variables and making them available for the whole class
    def __init__(self, to, subject, body, path=None, filename=None, msg=None):
        self.to = to
        self.subject = subject
        self.body = body
        self.msg = msg
        status = "Not Drafted"
        self.status = status
        if path != None:
            self.path = path
            self.filename = filename
    
    
    #Option to draft the email in advance if it is to be sent in a hurry
    def create_draft(self, user):
        #Creating the instance of MIMEMultipart to format the email
        data = MIMEMultipart()
        data['From'] = user
        data['To'] = (self.to)
        data['Subject'] = (self.subject)
        data.attach(MIMEText((self.body), 'plain'))

        #Adding the attachment if a path is given 
        if (self.path) != None:
            attachment = open((self.path), "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % (self.filename))
            data.attach(p)
        (self.status) = "Drafted"
        (self.msg) = data.as_string()
        print("Drafted")
        

    #Creating the email if not already drafted and sending it using smtplib
    def send(self, user, password):
        #The email creation
        if self.status == "Not Drafted":
            data = MIMEMultipart()
            data['From'] = user
            data['To'] = (self.to)
            data['Subject'] = (self.subject)
            data.attach(MIMEText((self.body), 'plain'))

            #The attachment part
            if (self.path) != None:
                attachment = open((self.path), "rb")
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= %s" % (self.filename))
                data.attach(p)
            (self.msg) = data.as_string()
            print("Drafted again")
        
        #Setting up the server
        server = SMTP("smtp.gmail.com", 587)
        server.starttls()
        #Loging in
        server.login(user, password)
        (message) = (self.msg)
        server.sendmail(user, (self.to), message)

        print("Email has been sent")
        server.quit()


if __name__ == "__main__":
    design = send_email(
        "swayamgavankar007@gmail.com",
        "Design sent",
        "Design has been sent",
        r"C:\Two-Storey Home\Elevation\renders\Front.png",
        "Front.png"
    )
    design.create_draft("swayamgavankar007@gmail.com")
    #_path = r"D:\Programming\Python\Python_Scripts\My_Design1_24.05.jpg"
    #file = "My_Design1_24.05.jpg"

    design.send("swayamgavankar007@gmail.com", "swayam2008")
#Thanks for using my small attempt towards Object-Oriented Programming