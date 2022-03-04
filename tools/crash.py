# Import modules
import os
import platform
import re
import sys
from time import ctime

from colorama import Fore

""" This function will stop the program when a critical error occurs """


def CriticalError(message, error):
    print(f"""
    {Fore.RED}:=== Critical error:
    {Fore.MAGENTA}MESSAGE: {message}.
    {Fore.MAGENTA}ERROR: {error}
    {Fore.RED}:=== Python info:
    {Fore.MAGENTA}PYTHON VERSION: {platform.python_version()}
    {Fore.MAGENTA}PYTHON BUILD: {'{}, DATE: {}'.format(*platform.python_build())}
    {Fore.MAGENTA}PYTHON COMPILER: {platform.python_compiler()}
    {Fore.MAGENTA}SCRIPT LOCATION: {os.path.dirname(os.path.realpath(sys.argv[0]))}
    {Fore.MAGENTA}CURRENT LOCATION: {os.getcwd()}
    {Fore.RED}:=== System info:
    {Fore.MAGENTA}SYSTEM: {platform.system()}
    {Fore.MAGENTA}RELEASE: {platform.release()}
    {Fore.MAGENTA}VERSION: {platform.version()}
    {Fore.MAGENTA}ARCHITECTURE: {'{} {}'.format(*platform.architecture())}
    {Fore.MAGENTA}PROCESSOR: {platform.processor()}
    {Fore.MAGENTA}MACHINE: {platform.machine()}
    {Fore.MAGENTA}NODE: {platform.node()}
    {Fore.MAGENTA}TIME: {ctime()}
    {Fore.RED}:=== Report:
    {Fore.MAGENTA}Please report it here: https://github.com/LimerBoy/Impulse/issues/new
    {Fore.RESET}
    """)
    sys.exit(5)


def ChackDate():
    """
    Перевірка на коректність ведених данних
    :return:
    """
    import config
    if config.EMAIL_SEND_1 == config.EMAIL_SEND_2:
        print(f"""
                {Fore.RED}:=== Critical error:
                {Fore.MAGENTA}Схоже, що електронні адреси співпадають.
                Перевірьте, чи почтові адреси відрізняються config.py навпроти параметру EMAIL_SEND
                """)
        sys.exit(5)

    elif not bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$',config.EMAIL_SEND_1)) or  \
        (bool(config.EMAIL_SEND_2) and not bool(re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$',config.EMAIL_SEND_2))):
        print(f"""
        {Fore.RED}:=== Critical error:
        {Fore.MAGENTA}Схоже, що електрона почта не була додана або вона не коректна.
        Перевірте наявність почти в файлі config.py навпроти параметру EMAIL_SEND та її коректність.
        """)
        sys.exit(5)
    elif not bool(config.PASS_EMAIL_SEND_1) or (bool(config.EMAIL_SEND_2) and not bool(config.PASS_EMAIL_SEND_2)):
        print(f"""
        {Fore.RED}:=== Critical error:
        {Fore.MAGENTA}Схоже, пароль електроної почти не був доданий.
        Перевірьте наявність почти в файлі config.py навпроти параметру PASS_EMAIL_SEND
        """)
        sys.exit(5)
    return True


def CheckOpenFile():
    """
    Перевірка наявності файлів усіх важливих файлів
    :return:
    """
    try:
        import config
        open(config.PATH_GET_EMAIL)
        open(config.PATH_SEND_TEXT_1)
        open(config.PATH_SEND_TEXT_2)
        open(config.PATH_SEND_TEXT_3)
    except IOError as E:
        print(f"""
            {Fore.RED}:=== Critical error:
            {Fore.MAGENTA} Схоже не вдалося відкрити файл. Перевірьте, наявність файлу 
            {E}
            """)
        sys.exit(5)
    return True
