import requests
from getmac import get_mac_address
from colorama import init, Fore, Style
import os

init(autoreset=True)
W = Fore.WHITE
R = Fore.RED

def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def main():
    clear()
    print(f"{R}[+]{W} MY INFO - Created by AHSAN")
    try:
        ip = requests.get('https://api.ipify.org').text
        mac = get_mac_address()
        print(f"{R}[*]{W} Your IP: {ip}")
        print(f"{R}[*]{W} Your MAC: {mac}")
    except Exception as e:
        print(f"{R}[-]{W} Error: {e}")
    input(f"
{R}[+]{W} Press Enter to exit...")

if __name__ == "__main__":
    main()
