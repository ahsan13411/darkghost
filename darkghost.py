import requests
import json
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, PhoneNumberType
from getmac import get_mac_address
import os
import sys
import time
import socket
import platform
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Colors
W = Fore.WHITE
R = Fore.RED
RESET = Style.RESET_ALL

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    clear()
    print(f"{R} █████╗ ██╗  ██╗███████╗ █████╗ ███╗   ██╗     ███████╗ ██████╗ ██╗     ")
    print(f"{R}██╔══██╗██║  ██║██╔════╝██╔══██╗████╗  ██║     ██╔════╝██╔═══██╗██║     ")
    print(f"{R}███████║███████║███████╗███████║██╔██╗ ██║     ███████╗██║   ██║██║     ")
    print(f"{R}██╔══██║██╔══██║╚════██║██╔══██║██║╚██╗██║     ╚════██║██║▄▄ ██║██║     ")
    print(f"{R}██║  ██║██║  ██║███████║██║  ██║██║ ╚████║     ███████║╚██████╔╝███████╗")
    print(f"{R}╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝     ╚══════╝ ╚══▀▀═╝ ╚══════╝")
    
    print(f"\n{W}================================================================================")
    print(f"{W}           [ {R}DARK GHOST {W}| {R}VERSION 1.6 {W}  ]")
    print(f"{W}           [ {R}Fuck Society. CREATED BY AHSAN. {W} ]")
    print(f"{W}================================================================================")
    
    # NODE INFO
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hostname = socket.gethostname()
        try:
            ipv4 = requests.get('https://api.ipify.org', timeout=5).text
        except:
            ipv4 = "Offline"
        mac = get_mac_address()
        device = f"{platform.system()} {platform.machine()}"
        kernel = platform.version()
    except:
        timestamp = hostname = ipv4 = mac = device = kernel = "Unknown"

    print(f"\n{R}[NODE INFO]")
    print(f"{W}┌─ timestamp : {R}{timestamp}")
    print(f"{W}├─ hostname  : {R}{hostname}")
    print(f"{W}├─ ipv4      : {R}{ipv4}")
    print(f"{W}├─ mac       : {R}{mac}")
    print(f"{W}├─ device    : {R}{device}")
    print(f"{W}└─ kernel    : {R}{kernel}")
    
    print(f"\n{W}================================================================================")
    print(f"{R}SIGINT: Halt  {W}SIGTSTP: Suspend")
    print(f"{W}Created by {R}AHSAN{W}. Our democracy has been hacked.")
    print(f"{W}================================================================================")

def ip_tracker():
    banner()
    print(f"\n{R}[+]{W} IP TRACKER (ADVANCED)")
    ip = input(f"{R}[?]{W} Enter IP Address: ")
    try:
        fields = "status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
        response = requests.get(f"http://ip-api.com/json/{ip}?fields={fields}")
        data = response.json()
        
        if data.get('status') == 'success':
            print(f"\n{W}========== {R}FULL IP INFORMATION {W}==========")
            print(f"{R}[*]{W} IP Address    : {R}{data.get('query')}")
            print(f"{R}[*]{W} Continent     : {W}{data.get('continent')} ({data.get('continentCode')})")
            print(f"{R}[*]{W} Country       : {W}{data.get('country')} ({data.get('countryCode')})")
            print(f"{R}[*]{W} Region        : {W}{data.get('regionName')} ({data.get('region')})")
            print(f"{R}[*]{W} City          : {W}{data.get('city')}")
            print(f"{R}[*]{W} District      : {W}{data.get('district', 'N/A')}")
            print(f"{R}[*]{W} Zip Code      : {W}{data.get('zip')}")
            print(f"{R}[*]{W} Latitude      : {W}{data.get('lat')}")
            print(f"{R}[*]{W} Longitude     : {W}{data.get('lon')}")
            print(f"{R}[*]{W} Timezone      : {W}{data.get('timezone')}")
            print(f"{R}[*]{W} UTC Offset    : {W}{data.get('offset')}")
            print(f"{R}[*]{W} Currency      : {W}{data.get('currency')}")
            print(f"{R}[*]{W} ISP           : {W}{data.get('isp')}")
            print(f"{R}[*]{W} Organization  : {W}{data.get('org')}")
            print(f"{R}[*]{W} AS            : {W}{data.get('as')}")
            print(f"{R}[*]{W} AS Name       : {W}{data.get('asname')}")
            print(f"{R}[*]{W} Reverse DNS   : {W}{data.get('reverse')}")
            
            print(f"\n{W}========== {R}NETWORK STATUS {W}==========")
            print(f"{R}[*]{W} Mobile Network: {R if data.get('mobile') else W}{data.get('mobile')}")
            print(f"{R}[*]{W} Proxy/VPN/Tor : {R if data.get('proxy') else W}{data.get('proxy')}")
            print(f"{R}[*]{W} Hosting       : {R if data.get('hosting') else W}{data.get('hosting')}")
            print(f"{W}======================================")
        else:
            print(f"{R}[-]{W} Error: {data.get('message', 'Invalid IP Address')}")
    except Exception as e:
        print(f"{R}[-]{W} Error: {e}")
    input(f"\n{R}[+]{W} Press Enter to go back...")

def my_info():
    banner()
    print(f"\n{R}[+]{W} YOUR IP & MAC INFO")
    try:
        ip = requests.get('https://api.ipify.org', timeout=5).text
        mac = get_mac_address()
        print(f"\n{W}========== {R}YOUR INFORMATION {W}==========")
        print(f"{R}[*]{W} Public IP Address : {R}{ip}")
        print(f"{R}[*]{W} MAC Address       : {R}{mac}")
        print(f"{W}==========================================")
    except Exception as e:
        print(f"{R}[-]{W} Error: {e}")
    input(f"\n{R}[+]{W} Press Enter to go back...")

def phone_tracker():
    banner()
    print(f"\n{R}[+]{W} PHONE TRACKER (ADVANCED)")
    number = input(f"{R}[?]{W} Enter Number (with +): ")
    try:
        parsed_number = phonenumbers.parse(number)
        
        # Basic Info
        location = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        # Number Type
        number_type = phonenumbers.number_type(parsed_number)
        type_str = "Unknown"
        if number_type == PhoneNumberType.MOBILE: type_str = "Mobile"
        elif number_type == PhoneNumberType.FIXED_LINE: type_str = "Fixed Line"
        elif number_type == PhoneNumberType.FIXED_LINE_OR_MOBILE: type_str = "Fixed Line or Mobile"
        elif number_type == PhoneNumberType.TOLL_FREE: type_str = "Toll Free"
        elif number_type == PhoneNumberType.VOIP: type_str = "VOIP"
        
        # Formats
        international = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        national = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        e164 = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        print(f"\n{W}========== {R}PHONE INFORMATION {W}==========")
        print(f"{R}[*]{W} International : {R}{international}")
        print(f"{R}[*]{W} National      : {W}{national}")
        print(f"{R}[*]{W} E164 Format   : {W}{e164}")
        print(f"{R}[*]{W} Location      : {W}{location}")
        print(f"{R}[*]{W} Carrier       : {W}{service_provider}")
        print(f"{R}[*]{W} Timezone      : {W}{', '.join(time_zones)}")
        print(f"{R}[*]{W} Number Type   : {W}{type_str}")
        print(f"{R}[*]{W} Valid Number  : {R if phonenumbers.is_valid_number(parsed_number) else W}{phonenumbers.is_valid_number(parsed_number)}")
        print(f"{R}[*]{W} Possible      : {W}{phonenumbers.is_possible_number(parsed_number)}")
        print(f"{W}==========================================")
        
    except Exception as e:
        print(f"{R}[-]{W} Error: {e}")
    input(f"\n{R}[+]{W} Press Enter to go back...")

def username_tracker():
    banner()
    print(f"\n{R}[+]{W} USERNAME TRACKER (SOCIAL SCAN)")
    username = input(f"{R}[?]{W} Enter Username: ")
    
    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
        {"url": "https://www.github.com/{}", "name": "GitHub"},
        {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
        {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
        {"url": "https://www.youtube.com/{}", "name": "Youtube"},
        {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
        {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
        {"url": "https://www.behance.net/{}", "name": "Behance"},
        {"url": "https://www.medium.com/@{}", "name": "Medium"},
        {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
        {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
        {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
        {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
        {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
        {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
        {"url": "https://www.ello.co/{}", "name": "Ello"},
        {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
        {"url": "https://www.telegram.me/{}", "name": "Telegram"},
        {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
    ]
    
    print(f"\n{W}========== {R}SHOW INFORMATION USERNAME {W}==========")
    print()
    
    for site in social_media:
        url = site['url'].format(username)
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f" {W}[ {R}+ {W}] {site['name']} : {R}{url}")
            else:
                print(f" {W}[ {R}+ {W}] {site['name']} : {W}Username not found !")
        except:
            print(f" {W}[ {R}+ {W}] {site['name']} : {W}Error checking site !")
            
    input(f"\n{R}[+]{W} Press Enter to go back...")

def main():
    while True:
        banner()
        print(f"\n{W}[ {R}1 {W}] {R}IP Tracker ")
        print(f"{W}[ {R}2 {W}] {R}Show Your IP ")
        print(f"{W}[ {R}3 {W}] {R}Phone Number Tracker")
        print(f"{W}[ {R}4 {W}] {R}Username Tracker")
        print(f"{W}[ {R}0 {W}] {R}Exit")
        
        choice = input(f"\n{R}[?]{W} Choose an option: ")
        
        if choice == '1':
            ip_tracker()
        elif choice == '2':
            my_info()
        elif choice == '3':
            phone_tracker()
        elif choice == '4':
            username_tracker()
        elif choice == '0':
            print(f"\n{R}[*]{W} Goodbye!")
            sys.exit()
        else:
            print(f"{R}[-]{W} Invalid Choice!")
            time.sleep(1)

if __name__ == "__main__":
    main()
