import requests
import os
import sys 


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def header():

    print(" /$$        /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$      /$$         /$$")
    print("| $$       /$$__  $$ /$$__  $$ /$$__  $$|__  $$__/| $$_____/    /$$$$       /$$$$")  
    print("| $$      | $$  \ $$| $$  \__/| $$  \ $$   | $$   | $$         |_  $$      |_  $$")  
    print("| $$      | $$  | $$| $$      | $$$$$$$$   | $$   | $$$$$ /$$$$$$| $$        | $$")  
    print("| $$      | $$  | $$| $$      | $$__  $$   | $$   | $$__/|______/| $$        | $$") 
    print("| $$      | $$  | $$| $$    $$| $$  | $$   | $$   | $$           | $$        | $$")  
    print("| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$   | $$   | $$$$$$$$    /$$$$$$ /$$ /$$$$$$")
    print("|________/ \______/  \______/ |__/  |__/   |__/   |________/   |______/|__/|______/\n \n")
                                                                                   
                                                                                                                                                                                                                                                                                                                  
    print("-" * 100 + "\n", "\n")

def lookup():

    ip_address = input(str("Enter an IP Address: \n"))
    

    response = requests.get(f"http://ip-api.com/json/{ip_address}").json()

    country = response["country"]
    state = response["regionName"]
    city = response["city"]
    isp = response["isp"]

    print(f"The location of the IP Address: {country}, {city}, {state} - {isp}")



def menu():

    print("What service would you like to perform?\n")
    print("1. Geolocation\n \n")

    choice = input(str("Enter Your Choice Here? "))

    if choice == "1" or "1 " or "1.0":
        cls()
        
    else:
        print("Please enter a valid choice.")




header()
menu()
lookup()
