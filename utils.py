import os
from time import sleep

def sleep_menu(time: int = 2):
    sleep(time)


def clear_console():
    if os.name == "nt":  # Sistema Windows
        os.system("cls")
    else:
        os.system("clear")  # Sistema Linux o Mac