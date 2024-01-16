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
    """
    Welcomes the user to the game and ask if the user
    have the courage to play.
    """
    print()
    print()
    txt1 = "Welcome to "
    new_str = txt1.center(80)
    print(Fore.WHITE + new_str)
    print()
    """ ASCII art """
    result = pyfiglet.figlet_format(
        "The Lost Island", font="cybermedium", justify="center")
    print(Fore.CYAN + result)

    txt2 = "Do you have the courage to enter this adventure?"
    new_str = txt2.center(80)
    print(Fore.WHITE + new_str)
    print()
    print()
    print()


welcome()


def userAnswer():
    """
    Prompt the the user to enter a answer.
    Different messages are displayed depending
    on the user's answer
    Is the users answer not valid, an error message
    with instructions is displayed
    """
    userAnswer = input(Fore.CYAN + "yes or no:\n\n")
    if (userAnswer == "no"):
        print()
        print("Oh! that's to bad. Maybe another time then :)")
        print()
    elif (userAnswer == "yes"):
        print()
        print("Good! The first thing you have to do is enter your name below:")
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
                    print(name + ", you are now about to begin perhaps")
                    print("your most exciting, fast-paced and dangerous")
                    print("adventure you have ever been on!")
                    input("So when you feel ready to begin just hit enter!\n")
                    break
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e} ")
    else:
        print()
        input(Fore.RED + "You must enter yes or no\n")


userAnswer()


def intro():
    print(" You and your friends went on a bout trip")


intro()
