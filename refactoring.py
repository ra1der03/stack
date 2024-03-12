import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Emails:
    def __init__(self, gmail_smtp, gmail_imap):
        self.gmail_smtp = gmail_smtp
        self.gmail_imap = gmail_imap
        self.log = 'login@gmail.com'
        self.password = 'qwerty'
        self.subject = 'Subject'
        self.recipients = ['vasya@email.com', 'petya@email.com']
        self.message = 'Message'
        self.header = None
        self.msg = MIMEMultipart()
        self.ms = smtplib.SMTP(self.gmail_smtp, 587)
        self.mail = imaplib.IMAP4_SSL(self.gmail_imap)
        self.mail.select('INBOX')
        self.criterion = ('(HEADER Subject "%s")' % self.header if self.header else 'ALL')
        self.result, self.data = self.mail.uid('search', 'None', self.criterion)
        self.latest_email_uid = self.data[0].split()[-1]
        self.result, self.data = self.mail.uid('fetch', self.latest_email_uid, '(RFC822)')
        self.raw_email = self.data[0][1]
        self.email_message = email.message_from_string(self.raw_email)

    # send message
    def send(self):
        self.msg['From'] = self.log
        self.msg['To'] = ', '.join(self.recipients)
        self.msg['Subject'] = self.subject
        self.msg.attach(MIMEText(self.message))

    def ms(self):
        # identify ourselves to smtp gmail client
        self.ms.login(self.log, self.password)
        self.ms.ehlo()
        # secure our email with tls encryption
        self.ms.starttls()
        # re-identify ourselves as an encrypted connection
        self.ms.ehlo()
        self.ms.sendmail(self.log, self.gmail_smtp, self.msg.as_string())
        self.ms.quit()

    def recieve(self):
        self.mail.login(self.log, self.password)
        self.mail.list()
        self.mail.select("inbox")
        assert self.data[0], 'There are no letters with current header'
        self.mail.logout()


em1 = "smtp.gmail.com"
em2 = "imap.gmail.com"

email1 = Emails(em1, em2)
print(email1)
