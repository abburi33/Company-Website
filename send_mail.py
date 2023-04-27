import ssl
import smtplib
import os


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("APPS_MAIL")
    password = os.getenv("PASSWORD_PYAPP")
    receiver = os.getenv("APPS_MAIL")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    def_message = """\
    Subject: YO!
    
    Toodles
    """
    send_mail(def_message)

