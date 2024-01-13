"""
Modules
"""
import sys
import os
import pyfiglet 
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def welcome():

    print()
    print()
    txt1 = "Welcome to "
    new_str = txt1.center(80)
    print(Fore.WHITE + new_str)
    print()
    result = pyfiglet.figlet_format("The Lost Island", font = "cybermedium" , justify="center") 
    print(Fore.CYAN + result)
    txt2 = "Do you have the courage to enter this adventure?"
    new_str = txt2.center(80)
    print(Fore.WHITE + new_str)
    print()
    print()
    input(Fore.CYAN+ "Enter yes or no\n")

welcome()




