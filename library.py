import smtplib
import os
import imaplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import config


def send_email(
        *,
        recipients: list[str],
        mail_body: str,
        mail_subject: str,
        attachment: str = None,
):
    SERVER = config.SMTP_SERVER
    PASSWORD = config.TOKEN_API
    USER = config.USER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = f'<Lection 14 user {USER}>'
    msg['To'] = ' ,'.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'

    if attachment:
        file_exists = os.path.exists(attachment)
        if not file_exists:
            print(f'file {attachment} does not exist')
        else:
            basename = os.path.basename(attachment)
            filesize = os.path.getsize(attachment)
            file = MIMEBase('application', f'octet-steam; name={basename}')
            file.set_payload(open(attachment, 'rb').read())
            file.add_header('Content-Desciption', f'attachment; filename={attachment}; size={filesize}')
            encoders.encode_base64(file)
            msg.attach(file)

    text_to_send = MIMEText(mail_body, 'plain')
    msg.attach(text_to_send)

    mail = smtplib.SMTP_SSL(SERVER)
    mail.login(USER, PASSWORD)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()


def check_email():
    PASSWORD = config.TOKEN_API
    USERNAME = config.USER
    SERVER = config.IMAP_SERVER
    imap = imaplib.IMAP4_SSL(SERVER)
    logged_in = imap.login(USERNAME, PASSWORD)
    # print(logged_in)
    # print(logged_in[1][-1].decode())
    # print(imap.search(None, 'UNSEEN'))


