import sys

import requests
from colorama import Fore


def InternetConnectionCheck():
    try:
        requests.get("https://google.com", timeout=4)
    except:
        print(
            f"{Fore.RED}[!] {Fore.MAGENTA}Your device is not connected to the Internet{Fore.RESET}"
        )
        sys.exit(1)
