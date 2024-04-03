GMAIL = 'smtp.gmail.com'
# NOTE: under this link https://myaccount.google.com/apppasswords add app pass in your account and use in your app - delete this pass after usage!
# 2-f authentication must be ON on google account
APP_PASS = 'to generATE'

import smtplib

my_email = 'mykhailo.trofimov@gmail.com'
guest_email = 'hamann.trofimov@gmail.com'
dron_email = 'andrii.linkoln@gmail.com'


def send_mail(message, subject, email):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # enable TLS - encrypt message
        connection.login(user=my_email, password=APP_PASS)

        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f'Subject: {subject}\n\n\n{message}')
