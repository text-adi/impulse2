from colorama import Fore


def flood(server, username, password: str, subject, body, target):
    """
    Відправляємо EMAIL.
    :param username: Електрона почта
    :param password: Пароль
    :param subject: Заголовок
    :param body: Основний текст
    :param target: Почта на яку відправляємо
    """

    msg = f"From: {username}\nSubject: {subject}\n{body}"
    # Send email
    try:
        server.sendmail(username, target, msg.encode('utf-8'))
    except Exception as err:
        print(
            f"{Fore.MAGENTA}Error while sending mail\n{Fore.MAGENTA}{err}{Fore.RESET}"
        )
        return False
    else:
        print(
            f"{Fore.GREEN}[+] {Fore.YELLOW}Mail sent to {target}.{Fore.RESET}"
        )
        return True

