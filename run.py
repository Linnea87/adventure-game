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


def print_slow(ltr):
    """
    Creates a slow typing effect.
    """
    for letter in ltr:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def clear():
    os.system("clear")


def welcome():
    """
    Welcomes the user to the game and ask if the user
    have the courage to play.
    """
    clear()
    print('')
    print_slow("\t\t\t\tWelcome to\n")
    print()
    time.sleep(1)
    """ ASCII art """
    result = pyfiglet.figlet_format(
        "The Lost Island", font="cybermedium", justify="center")
    print(Fore.CYAN + result)
    print('')
    print_slow("\t\tDo you have the courage to enter this adventure?\n")
    print('')
    print('')
    time.sleep(1)

welcome()


def player_answer():
    """
    Prompt the user to enter a answer.
    Different messages are displayed depending
    on the user's answer
    Is the users answer not valid, an error message
    with instructions is displayed
    """
    player_answer = input("yes or no:\n >> ")
    print()
    if player_answer == "yes":
        print()
        print_slow(
            "Good! The first thing you have to do is enter your name below:")
        print()
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
                    print_slow(
                        "your most exciting, fast-paced and dangerous\n")
                    print_slow("adventure you have ever been on!\n")
                    print_slow(
                        "\nSo when you feel ready to begin just hit enter!\n")
                    input()
                    break
            except Exception as e:
                   print(Fore.RED + f"An error occurred: {e}")
    
    elif player_answer == "no":
        print_slow("\nOh, that's to bad! Maybe another time then :)")
        time.sleep(2)
        print()
        print()
        sys.exit()
    else: 
        print(Fore.RED + 'Invalid answer, enter yes or no\n')
        input()
  
    

player_answer()


def intro():
    clear()
    print_slow("What was supposed to be a peaceful and delightful boat trip at sea\n") 
    print_slow("turned out to be the opposite.\n")
    print_slow("After weeks lost at sea a furocius storm hits the boat.\n")
    print_slow("Powerful waves and heavy rain destroys parts of your boat\n") 
    print_slow("and the boat starts to sink.\n")


intro()
