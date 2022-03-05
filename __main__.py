import codecs
import sys
import time
from datetime import datetime

from colorama import Fore

import config
from tools.EMAIL.emalTools import WriteSenderEmail

try:  # здійснюємо базові перевірки
    from tools.ipTolls import InternetConnectionCheck
    from tools.crash import CriticalError, CheckOpenFile, ChackDate
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.EMAIL.main import flood

    InternetConnectionCheck()
    CheckOpenFile()
    ChackDate()
except ImportError as err:
    CriticalError("Failed import some modules", err)
    sys.exit(1)


def add_first_line_email(email_send: str):
    """
    Видаляємо рядки з файлу з почтою, щоб при повторному перезапуску не відсилати повторно повідомлення
    :param path_to_email: шлях до файлу
    """
    f = open(config.PATH_GET_EMAIL_1, 'a')
    f.write(email_send + '\n')
    f.close()


def main(file_get_email):
    # print(f"{Fore.MAGENTA}Starting...\n{Fore.MAGENTA}{Fore.RESET}")
    # print(f"{Fore.MAGENTA}Wait...\n{Fore.MAGENTA}{Fore.RESET}")
    kilk_send_message = 0
    while datetime.now().time().second > 1:
        time.sleep(0.5)
        break

    server1, username1 = WriteSenderEmail(config.EMAIL_SEND_1, config.PASS_EMAIL_SEND_1)
    if bool(config.EMAIL_SEND_2):
        server2, username2 = WriteSenderEmail(config.EMAIL_SEND_2, config.PASS_EMAIL_SEND_2)
    else:
        server2, username2 = server1, username1

    try:
        file = open(config.PATH_GET_EMAIL_1, 'r')
    except Exception:
        open(config.PATH_GET_EMAIL_1, 'w').close()
        file = open(config.PATH_GET_EMAIL_1, 'r')

    list_email = file.read().split('\n')
    file.close()
    for get_email in file_get_email.read().split('\n'):  # читає список адрес

        try:
            if get_email == list_email[kilk_send_message]:
                # пропускаємо ті електроні адреси, які вже надіслалися
                kilk_send_message += 1
                continue
        except Exception:
            pass

        if kilk_send_message % 2:
            server, username, password = server1, username1, config.PASS_EMAIL_SEND_1

        else:
            server, username, password = server2, username2, config.PASS_EMAIL_SEND_2

        if kilk_send_message % 3 == 0:
            path = config.PATH_SEND_TEXT_1
        elif kilk_send_message % 3 == 1:
            path = config.PATH_SEND_TEXT_2
        else:
            path = config.PATH_SEND_TEXT_3
        kilk_send_message += 1

        # print(kilk_send_message)

        send_subject = config.SEND_SUBJECT
        new_path = codecs.open(path,'r', encoding='utf-8').read()
        if not flood(server, username, password, send_subject, new_path, get_email):
            sys.exit(1)
        add_first_line_email(get_email)

    print(f"{Fore.MAGENTA}[!] {Fore.BLUE}Attack completed!{Fore.RESET}")
    open(config.PATH_GET_EMAIL_1, 'w').close()  # після атаки очищемо файл


if __name__ == '__main__':
    try:
        main(open(config.PATH_GET_EMAIL))
    except KeyboardInterrupt:
        print(
            f"\n{Fore.RED}[!] {Fore.MAGENTA}Ctrl+C detected. Stopping ..{Fore.RESET}"
        )
    except Exception as err:
        print(err)
