import time
from rich import align
import random
from rich.progress import Progress
import os
import json

class auto_install():
    
    def is_package_installed(package):
        import pkg_resources
        try:
            pkg_resources.get_distribution(package)
            return True
        except pkg_resources.DistributionNotFound:
            return False
    
    def check_current_version():
        import platform
        version = platform.python_version()
        return version
    
    def install_latest_python():
        import subprocess
        subprocess.run(["pip", "install", "--upgrade", "python"])
        
    def install_package(package):
        import pip
        pip.main(['install', package])
        
def run_once():
    import pkg_resources
    try:
        
        package_verify = auto_install.is_package_installed("platform")
        
        if package_verify is False:
            print("Installing package 'request'.")
            auto_install.install_package("platform")
            print("Download finished...")
        else:
            pass
        
        print("Checking the Python version in your system...")
        time.sleep(1)
        
        current_version = auto_install.check_current_version()
        print("Python version is: ", current_version)
        
        if current_version >= '3.9':
            print('The current version of Python is 3.9 or newer')
        else:
            print('The current version of Python is older than 3.9')
            print('Updating Python version...')
            time.sleep(1)
            auto_install.install_latest_python()
            
        print("Downloading necessary packages...")
        
        auto_install.install_package("rich")
        auto_install.install_package("progress")
        
        print("All preparations are done.")
        time.sleep(5)
        
    except pkg_resources.DistributionNotFound:
        print("The Python package is not installed in this system.")


class loading_progress():
    
    def task1(self):
        with Progress() as progress:
            task = progress.add_task("[cyan]INITIALIZING PROGRAM PLEASE WAIT...",total=1000)
        
            while not progress.finished:
                progress.update(task, advance=7)
                time.sleep(0.02)
    def task2(self):
        with Progress() as progress:
            task = progress.add_task("[green]FETCHING THE ALGORITHM...",total=1000)
        
            while not progress.finished:
                progress.update(task, advance=7)
                time.sleep(0.02)

    def task3(self):
        with Progress() as progress:
            task = progress.add_task("[red]READING THE PROGRAM...",total=1000)
        
            while not progress.finished:
                progress.update(task, advance=7)
                time.sleep(0.02)
                
class ascii_art():
    def art1(self):
        print('''
                                  
░█████╗░██████╗░░░██╗██╗░█████╗░██╗░░██╗
██╔══██╗██╔══██╗░██╔╝██║██╔══██╗██║░██╔╝
██║░░╚═╝██████╔╝██╔╝░██║██║░░╚═╝█████═╝░
██║░░██╗██╔══██╗███████║██║░░██╗██╔═██╗░
╚█████╔╝██║░░██║╚════██║╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝
              
              
              Developed by: Styx
                    ''')

    
    def art2(self):
        print('''
                    
──────────────────────────────────────────────────────────────────────────────────
─██████████████─████████████████───██████──██████─██████████████─██████──████████─
─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░██─
─██░░██████████─██░░████████░░██───██░░██──██░░██─██░░██████████─██░░██──██░░████─
─██░░██─────────██░░██────██░░██───██░░██──██░░██─██░░██─────────██░░██──██░░██───
─██░░██─────────██░░████████░░██───██░░██████░░██─██░░██─────────██░░██████░░██───
─██░░██─────────██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██───
─██░░██─────────██░░██████░░████───██████████░░██─██░░██─────────██░░██████░░██───
─██░░██─────────██░░██──██░░██─────────────██░░██─██░░██─────────██░░██──██░░██───
─██░░██████████─██░░██──██░░██████─────────██░░██─██░░██████████─██░░██──██░░████─
─██░░░░░░░░░░██─██░░██──██░░░░░░██─────────██░░██─██░░░░░░░░░░██─██░░██──██░░░░██─
─██████████████─██████──██████████─────────██████─██████████████─██████──████████─
──────────────────────────────────────────────────────────────────────────────────
                    Developed by: Styx
                    ''')
        
    
    def art3(self):
        print('''                   
██████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░█
█░░▄▀░░█████████░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███
█░░▄▀░░█████████░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███
█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░███
█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░░░███░░░░░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███
█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█████████░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█
██████████████████████████████████████████████████████████████████████████████████
                    Developed by: Styx
                    ''')
        

def loading_bar():
    loading = loading_progress()
    task_list = [loading.task1, loading.task2, loading.task3]
    chosen_task = random.choice(task_list)
    chosen_task()

def art_gen():
    ascii = ascii_art()
    art_list = [ascii.art1, ascii.art2, ascii.art3]
    chosen_art = random.choice(art_list)
    chosen_art()

def create_cache():
    open('cache.txt', 'a').close()
    
    with open('cache.txt', 'w') as file:
        file.write('False')
        
def retrieve_from_cache():
    with open('cache.txt', 'r') as file:
        value = file.read()
        
        return value

def main():
    
    while True:
        if not os.path.exists('cache.txt'):
            create_cache()
            
        value = retrieve_from_cache()
        
        if value == 'False':
            run_once()
            with open('cache.txt', 'w') as file:
                file.write('True')
            print('Cache file value changed. Not executing this again.')
        else:
            pass
                
        loading_bar()
        os.system('cls')
        art_gen()
        time.sleep(3)
        print('\n Choose your option:')
        print("1. SSID Multiplied by 3 Method")
        print("2. Hex Conversion Method")
        print("3. PLDT Firmware Method")
        print("4. About")
        print("5. Exit")
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            ssid_by_3()
        elif choice == '2':
            hex_conversion()
        elif choice == '3':
            firmware_method()
        elif choice == '4':
            about()
        elif choice == '5':
            prog_exit()
        else:
            print("Invalid choice. Please try again.")
            
def ssid_by_3():
    os.system('cls')
    print('''
    Enter the integers of the PLDT WiFi located in your WiFi SSID.

    example: PLDTWIFI12345

    only input the integer.\n
          ''')
    
    while True:
        try:
            ssid = int(input("Enter the integer from your WiFi SSID: "))
            
            multiply = ssid * 3
            
            print("PLDT WiFI Password is: ", multiply)
            time.sleep(3)
            
            print('\nReturn to Main Menu?')
            choice = input('(Y/N) Enter other input to try again: ')
            
            if choice == 'y' or choice == 'Y':
                return main()
            elif choice == 'n' or choice == 'N':
                return prog_exit()
            else:
                return ssid_by_3()
        except ValueError:
            print("Invalid Input. Only input integer values.")
    
    
    
    
def hex_conversion():
    os.system('cls')
    print('''
    Enter the integers of the PLDT WiFi located in your WiFi SSID.

    example: PLDTWIFI12345

    only input the integer.\n
    
    Refer to the Dictionary for conversion.
    
    0 : f,
    1 : e,
    2 : d,
    3 : c,
    4 : b,
    5 : a,
    6 : 9,
    7 : 8,
    8 : 7,
    9 : 6,
    a : 5,
    b : 4,
    c : 3,
    d : 2,
    e : 1,
    f : 0,
    
          ''')
    
    hex_dict = {
    "0" : "f",
    "1" : "e",
    "2" : "d",
    "3" : "c",
    "4" : "b",
    "5" : "a",
    "6" : "9",
    "7" : "8",
    "8" : "7",
    "9" : "6",
    "a" : "5",
    "b" : "4",
    "c" : "3",
    "d" : "2",
    "e" : "1",
    "f" : "0",
    }
    
    ssid = input("Enter the integer from your WiFi SSID: ")
    
    result = ""
    for char in ssid:
        mapped_char = hex_dict.get(char)
        if mapped_char is not None:
            result += mapped_char
        else:
            result += char
    
    
    print("PLDT WiFi Password is: ", result)
    time.sleep(3)
    
    print('\nReturn to Main Menu?')
    choice = input('(Y/N) Enter other input to try again: ')
            
    if choice == 'y' or choice == 'Y':
        return main()
    elif choice == 'n' or choice == 'N':
        return prog_exit()
    else:
        return hex_conversion()

def firmware_method():
    os.system('cls')
    print('''
          For Old PLDT Firmware. You only need the last 5 mac characters from your SSID.
          
          Example: PLDTFIBR_b12jsc
          
          You get. PLDTWIFI12JSC
          ''')
    
    print('\nReturn to Main Menu?')
    choice = input('(Y/N) Enter other input to try again: ')
            
    if choice == 'y' or choice == 'Y':
        return main()
    elif choice == 'n' or choice == 'N':
        return prog_exit()
    else:
        return firmware_method()

def about():
    os.system('cls')
    art_gen()
    time.sleep(3)
    print('''\n\n          
Welcome User to CR4CK!

This is just a simple program I make to kill time and make some progres of my knowledge in the programming field.
The program is intended only for PLDT WiFi with default password. It uses the WiFi's SSID to crack the password,
using the following methods given in this program. This is just to help you crack the password easily without the
use of paper and pen. 

If you want to crack password that are changed already, you can use Brute Force or other tools that would crack
WiFi handshakes. Also, cracking or hacking is illegal so, do it ethically.

Have a Great Day!

Program Developed by: Styx
          ''')
    
    print('\n\nReturn to Main Menu?')
    choice = input('(Y/N): ')
    
    if choice == 'y' or choice == 'Y':
        return main()
    else:
        return prog_exit()

def prog_exit():
    os.system('cls')
    print('This will exit the program, are you sure you want to exit?')
    choice = input('(Y/N): ')
    
    if choice == 'y' or choice == 'Y':
        return exit()
    else:
        print("Returning to Menu...")
        return main()
    
if __name__ == '__main__':
    main()