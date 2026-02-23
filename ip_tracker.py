import requests
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
    print(f"{R}[+]{W} IP TRACKER - Created by AHSAN")
    ip = input(f"{R}[?]{W} Enter IP Address: ")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            print(f"{R}[*]{W} IP: {data['query']}")
            print(f"{R}[*]{W} Country: {data['country']}")
            print(f"{R}[*]{W} Region: {data['regionName']}")
            print(f"{R}[*]{W} City: {data['city']}")
            print(f"{R}[*]{W} ISP: {data['isp']}")
            print(f"{R}[*]{W} Org: {data['org']}")
            print(f"{R}[*]{W} AS: {data['as']}")
            print(f"{R}[*]{W} Lat/Lon: {data['lat']}, {data['lon']}")
        else:
            print(f"{R}[-]{W} Invalid IP Address.")
    except Exception as e:
        print(f"{R}[-]{W} Error: {e}")
    input(f"
{R}[+]{W} Press Enter to exit...")

if __name__ == "__main__":
    main()
