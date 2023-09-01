import library


def main():
    recipients = ['molly_mail@ukr.net']
    mail_body = 'Text from me'
    mail_subject = "Hello"
    attachment = 'library.py'
    library.send_email(
        recipients=recipients,
        mail_body=mail_body,
        mail_subject=mail_subject,
        attachment=attachment
    )


if __name__ == '__main__':
    main()
