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


def print_slow(ltr, color=Fore.RESET):
    """
    Creates a slow typing effect, with the options to change the text color.
    """
    for letter in ltr:
        sys.stdout.write(color + letter)
        sys.stdout.flush()
        time.sleep(0.1)
        

def clear():
    """
    This function clears the screen from written text.
    """
    os.system("clear")


def welcome():
    """
    Welcomes the user to the game and ask if the user
    have the courage to play.
    """
    clear()
    print()
    print_slow("\t\t\t\tWelcome to\n")
    print()
    time.sleep(1)
    """ ASCII art """
    result = pyfiglet.figlet_format(
        "The Lost Island", font="cybermedium", justify="center")
    print(Fore.CYAN + result)
    print_slow("\t\tDo you have the courage to enter this adventure?\n")
    print()
    time.sleep(1)
    print(Fore.GREEN + "yes or no:\n")
    print()
    


def player_answer():
    """
    Prompt the user to enter a answer.
    Different messages are displayed depending
    on the user's answer
    Is the users answer not valid, an error message
    with instructions is displayed
    """
    answer = input(Fore.YELLOW + ">> ")
    print()
    while answer not in ("yes", "no"):
        print(Fore.RED + "Invalid answer, enter yes or no!")
        print()
        answer = input(Fore.YELLOW + ">> ")
    if answer == "no":
        print_slow("Oh, that's to bad! Maybe another time then :)\n")
        time.sleep(1)
        print()
        print()
        sys.exit()
    elif answer == "yes":
        print()
        print_slow(
            "Good! The first thing you have to do is enter your name below:")
        print()
        print()


def player_name():
    """
    Prompt the user to enter a name. The name is required,
    if the name contains other than letters or
    is shorter than 3 letters,
    an error with instructions is displayed
    """
   
    while True:
        try:
            global name 
            name = input(Fore.YELLOW + ">> ")
            if not name.isalpha():
                print()
                print(Fore.RED + "Your name can only contain letters!")
            elif len(name) < 3:
                print()
                print(Fore.RED + "Your name needs to be 3 letters or more!")
            else:
                print()
                print_slow(name + ", you are now about to begin perhaps\n")
                print_slow(
                    "your most exciting, fast-paced and dangerous\n")
                print_slow("adventure you have ever been on!\n")
                print_slow(
                    "So when you feel ready to begin just hit enter!\n")
                input()
                break
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")


def intro():
    """
    The game adveture starts here.
    """
    clear()
    print()
    print_slow("What was supposed to be a quiet and ")
    print_slow("lovely boating holiday\nout at sea ")
    print_slow("with some of your closest friends, ")
    print_slow("turned out\nto be the complete opposite!\n")
    print()
    print_slow("After a few days, you end up in the eye of the worst storm\n")
    print_slow("you've ever experienced. ")
    print_slow("The heavy rain and the powerful waves\n")
    print_slow("destroy parts of your boat and it slowly begins to sink.\n")
    print_slow("In a panic, you try to get to the lifeboat ")
    print_slow("to save you\nand your friends, ")
    print_slow("when suddenly you collapse\nand everything goes dark!\n")
    time.sleep(1)


def the_waking_up():
    """
    The user must interact so that the story progresses.
    """
    clear()
    print()
    print_slow("- come on " + name + " you can't die and leave me alone here!\n", Fore.BLUE)
    time.sleep(1)
    print()
    print_slow("You hear a voice far off in the distance ") 
    print_slow("calling\nout to you and you begin to regain consciousness.\n")
    time.sleep(1)
    print()
    print(Fore.GREEN + "Press w for waking up:\n")
    input(Fore.YELLOW + ">> ")
    print()
    print_slow("Slowly you open your eyes and see your friend\n") 
    print_slow("Oliwer leaning over you!\n")
    time.sleep(1)
        
    
def the_stranded_friends():
    """
    The user must interact so that the story progresses.
    """
    clear()
    print()
    print_slow("You sit up slowly and your head aches.\n")
    print_slow("When you bring your hand to your head, you feel a bump.\n")
    print()
    print(Fore.GREEN + "Press t for talk to Oliwer:\n")
    input(Fore.YELLOW + ">> ")
    print()
    print_slow("- what happened? where are we?\n", Fore.YELLOW)
    time.sleep(1)
    print()
    print_slow("- The boat sank. When I woke up I found you lying a few meters away.\n", Fore.BLUE)
    print_slow("  I ran as fast as I could to give you first aid.\n", Fore.BLUE)
    print_slow("  The waves seem to have driven us to some sort of island.\n", Fore.BLUE)
    print()
    print_slow("Oliwer extends his hand to help you up\n")
    print()
    time.sleep(1)
    print(Fore.GREEN + "Press h to take Oliwers hand\n")
    input(Fore.YELLOW + ">> ")
  
def the_shelter(): 
    """
    The user most enter a choice. 
    Each choice has different stories 
    but both lead the user further in the game.
    Are the choice not valid an error message
    with instructions is displayed
    """
    clear()
    print()
    print_slow("- What do you think " + name + ", should we try to build\n", Fore.BLUE)
    print_slow("  a shelter here on the beach or should we\n", Fore.BLUE)
    print_slow("  go further into the island to seek shelter for the night?\n", Fore.BLUE)
    print()
    print(Fore.GREEN + "build or seek:\n")
    choice = input(Fore.YELLOW + ">> ")
    while choice not in ("build", "seek"):
        print()
        print(Fore.RED + "Invalid choice, you must choose build or seek!")
        print()
        choice = input(Fore.YELLOW + ">> ")
        print()
    if choice == "build":
        print()
        print_slow("You and Oliwer start looking for driftwood\n") 
        print_slow("that you can use to build a shelter.\n")
        print_slow("After an hour of searching you start to get hungry\n")
        print_slow("and realize that it is hopeless to find any driftwood\n")
        print_slow("Finally you decide to go further into the island to look\n")
        print_slow("for something to eat and find some sort of shelter for the night.\n")
    elif choice == "seek":
        print_slow() 
   
def chapter_4():
    print()
    
    

def chapter_5():
    print()
    
def end_scen_1():
    print()

def end_scen_2():
    print()


def main():
    """
    This function calls all the other functions.
    """
    welcome()
    player_answer()
    player_name()
    intro()
    the_waking_up()
    the_stranded_friends()
    the_shelter()
    chapter_4()
    chapter_5()
    end_scen_1()
    end_scen_2()
    


main()
