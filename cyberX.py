#!/usr/bin/env python3

import os
import random
import string
import time

# Colors
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
cyan = "\033[96m"
reset = "\033[0m"

def clear():
    os.system("clear")

def banner():
    print(cyan + """
   ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██╗  ██╗
  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝ ╚███╔╝
  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗ ██╔██╗
  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██╔╝ ██╗
   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
    """ + reset)

    print(yellow + "        Welcome to CyberX Toolkit")
    print("        Developer: Sujeet\n" + reset)

def loading():
    print(green + "[*] Initializing modules..." + reset)
    time.sleep(1)

def system_info():
    os.system("uname -a")

def ip_info():
    os.system("ip a")

def storage_info():
    os.system("df -h")

def show_time():
    os.system("date")

def password_generator():
    length = 12
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    print(green + "\nGenerated Password: " + password + reset)

def menu():

    while True:
        print(cyan + """
========= CyberX Control Panel =========

[1] System Information
[2] IP Address
[3] Storage Usage
[4] Date & Time
[5] Password Generator
[6] Exit

========================================
""" + reset)

        choice = input("CyberX > ")

        if choice == "1":
            system_info()

        elif choice == "2":
            ip_info()

        elif choice == "3":
            storage_info()

        elif choice == "4":
            show_time()

        elif choice == "5":
            password_generator()

        elif choice == "6":
            print(red + "\nExiting CyberX Toolkit...\n" + reset)
            break

        else:
            print(red + "Invalid option!\n" + reset)

clear()
banner()
loading()
menu()
