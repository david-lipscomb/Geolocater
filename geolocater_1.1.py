import requests
import os
import sys
from colorama import Fore 


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def header():

    print(f"{Fore.LIGHTGREEN_EX} /$$        /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$      /$$         /$$")
    print(f"| $$       /$$__  $$ /$$__  $$ /$$__  $$|__  $$__/| $$_____/    /$$$$       /$$$$")  
    print(f"| $$      | $$  \ $$| $$  \__/| $$  \ $$   | $$   | $$         |_  $$      |_  $$")  
    print(f"| $$      | $$  | $$| $$      | $$$$$$$$   | $$   | $$$$$ /$$$$$$| $$        | $$")  
    print(f"{Fore.MAGENTA}| $$      | $$  | $$| $$      | $$__  $$   | $$   | $$__/|______/| $$        | $$") 
    print(f"| $$      | $$  | $$| $$    $$| $$  | $$   | $$   | $$           | $$        | $$")  
    print(f"| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$   | $$   | $$$$$$$$    /$$$$$$ /$$ /$$$$$$")
    print(f"|________/ \______/  \______/ |__/  |__/   |__/   |________/   |______/|__/|______/\n \n")
                                                                                   
                                                                                                                                                                                                                                                                                                                  
    print("-" * 100 + f"{Fore.RESET}\n", "\n")

def lookup():

    ip_address = input(str("Enter an IP Address: \n"))
    

    response = requests.get(f"http://ip-api.com/json/{ip_address}").json()

    country = response["country"]
    state = response["regionName"]
    city = response["city"]
    isp = response["isp"]

    print(f"The location of the IP Address: {country}, {city}, {state} - {isp}")



def menu():

    print(f"{Fore.LIGHTGREEN_EX}What service would you like to perform?\n")
    print("1. Geolocation\n \n")

    choice = input(str("Enter Your Choice Here? "))

    if choice == "1" or "1 " or "1.0":
        cls()
        
    else:
        print("Please enter a valid choice.")




header()
menu()
lookup()
