"""
Modules
"""
import sys
import os
import time
import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def print_slow(text):
    """
    Creates a slow typing effect.
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

def input_slow(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05) 
    value = input()  
  return value  


def clear():
    os.system("clear")

def welcome():
    """
    Welcomes the user to the game and ask if the user
    have the courage to play.
    """
    clear()
    print()
    print()
    txt1 = "Welcome to\n"
    new_str = txt1.center(80)
    print_slow(Fore.WHITE + new_str)
    time.sleep(2)
    print()
    """ ASCII art """
    result = pyfiglet.figlet_format(
        "The Lost Island", font="cybermedium", justify="center")
    print(Fore.CYAN + result)
    txt2 = "Do you have the courage to enter this adventure?\n"
    new_str = txt2.center(80)
    print_slow(Fore.WHITE + new_str)
    print()
    print()
    print()
    time.sleep(2)

welcome()


def userAnswer():
    """
    Prompt the user to enter a answer.
    Different messages are displayed depending
    on the user's answer
    Is the users answer not valid, an error message
    with instructions is displayed
    """
    userAnswer = input(Fore.CYAN + "yes or no:\n")
    if (userAnswer == "yes"):
        print()
        print_slow("Good! The first thing you have to do is enter your name below:")
        print()
        while True:
            """
            Ask the user for a name. The name is required
            if the name contains other than letters or
            is shorter than 3 letters,
            an error with instructions is displayed
            """
            try:
                name = input("")
                if not name.isalpha():
                    print()
                    print(
                        Fore.RED + "Your name can only contain letters!"
                    )
                elif len(name) < 3:
                    print()
                    print(
                        Fore.RED + "Your name needs to be 3 letters or more!")
                else:
                    print()
                    print_slow(name + ", you are now about to begin perhaps\n")
                    print_slow("your most exciting, fast-paced and dangerous\n")
                    print_slow("adventure you have ever been on!\n")
                    print()
                    print()
                    input_slow("So when you feel ready to begin just hit enter!\n")
                    break
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e} ")
    elif (userAnswer == "no"):
        print()
        print_slow("Oh! that's to bad. Maybe another time then :)")
        print()
        time.sleep(2) 
    else:
        print('')
        input(Fore.RED + "You must enter yes or no\n")
        print('')


userAnswer()


def intro():
        print(" You and your friends went on a bout trip")

intro()


