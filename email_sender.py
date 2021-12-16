import smtplib
from user import User
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class EmailService:
    sender: str = 'cxi.secret.santa@gmail.com'
    password: str = 'Fantast!c4'
    subject:str = 'Your Secret Child Is....'
    santa: User

    def __init__(self, santa:User):
        self.santa = santa

    def prepare_mail_content(self):
        mail_content = "<HTML><h2>Hello Santa {0},</h2><br> <img src='cid:image'><br><h3> Your secret child is {1}.<br><br>Best of Luck.</h3>"
        msgText = MIMEText(mail_content.format(self.santa.name, self.santa.secret_child), 'html')
        mime_message = MIMEMultipart('alternative')
        mime_message.attach(msgText)
        return mime_message

    def insert_image(self):
        image_file = open('christmas.jpeg', 'rb')
        msgImage = MIMEImage(image_file.read())
        msgImage.add_header('Content-ID', '<image>')
        image_file.close()
        return msgImage

    def prepare_mail(self):
        message = MIMEMultipart('related')
        message['From'] = self.sender
        message['To'] = self.santa.email
        message['Subject'] = 'Your Secret Child Is....'
        message.attach(self.prepare_mail_content())
        message.attach(self.insert_image())
        return message


    def send_mail(self):
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(self.sender, self.password) #login with mail_id and password
        session.sendmail(self.sender, self.santa.email, self.prepare_mail().as_string())
        session.quit()
        print('Mail Sent successfully to ', self.santa.email)
