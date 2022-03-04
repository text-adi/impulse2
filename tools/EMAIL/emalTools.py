import sys
from getpass import getuser
from smtplib import SMTPAuthenticationError, SMTP

# File with login data
from colorama import Fore

sender_email_database = "tools/EMAIL/sender.json"
twilight_encryption_key = getuser() + ":TWILIGHT"
smtp_server = "smtp.gmail.com"
smtp_port = 587

""" Write sender email """


def WriteSenderEmail(username: str, password: str):
    """
    Перевіряємо підключення
    :param username:
    :param password:
    :return:
    """
    server = SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    # Try login to gmail account
    try:
        server.login(username, password)
    except SMTPAuthenticationError:
        print(
            f"{Fore.RED}[!] {Fore.MAGENTA}Wrong password from account or try enable this:"
            f"\n    https://myaccount.google.com/lesssecureapps{Fore.RESET}"
        )
        sys.exit(1)
    else:
        print(
            f"{Fore.GREEN}[+] {Fore.YELLOW}Successfully logged in{Fore.YELLOW} {username}{Fore.RESET}"
        )

    return [server, username]
