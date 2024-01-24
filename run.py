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
    print_slow("\n\t\t\t\tWelcome to\n\n")
    time.sleep(1)
    """ ASCII art """
    result = pyfiglet.figlet_format(
        "The Lost Island", font="cybermedium", justify="center")
    print(Fore.CYAN + result)
    print_slow("\t\tDo you have the courage to enter this adventure?\n\n")
    time.sleep(1)
    print(Fore.GREEN + "yes or no:\n")
    

def player_answer():
    """
    Prompt the user to enter a answer.
    Different messages are displayed depending
    on the user's answer
    Is the users answer not valid, an error message
    with instructions is displayed
    """
    answer = input(Fore.YELLOW + ">> ")
    while answer not in ("yes", "no"):
        print(Fore.RED + "\nInvalid answer, enter yes or no!\n")
        answer = input(Fore.YELLOW + ">> ")
    if answer == "no":
        print_slow("\nOh, that's to bad! Maybe another time then :)\n\n")
        time.sleep(1)
        sys.exit()
    elif answer == "yes":
        clear()
        print_slow(
            "\nGood! The first thing you have to do is enter your name below:\n\n")


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
                print(Fore.RED + "\nYour name can only contain letters!")
            elif len(name) < 3:
                print(Fore.RED + "\nYour name needs to be 3 letters or more!")
            else:
                clear()
                print_slow(
                    "\n" + name + ", you are now about to begin perhaps\n"
                    "your most exciting, fast-paced and dangerous\n"
                    "adventure you have ever been on!\n\n")
                input("So when you feel ready to begin just hit enter!" )
                break
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")


def intro():
    """
    The adventure game starts with an exciting intro 
    using the print_slow function
    """
    clear()
    print_slow(
        "\nWhat was supposed to be a quiet and "
        "lovely boating holiday\nout at sea "
        "with some of your closest friends, turned out\n"
        "to be the complete opposite!\n\n"
        "After a few days, you end up in the eye of the worst storm\n"
        "you've ever experienced. "
        "The heavy rain and the powerful waves\n"
        "destroy parts of your boat and it slowly begins to sink.\n"
        "In a panic, you try to get to the lifeboat "
        "to save you\nand your friends, "
        "when suddenly you collapse\n"
        "and everything goes dark!\n")
    time.sleep(1)


def the_stranded_friends():
    """
    With help of the input function, the user must 
    interact so that the story progresses.
    """
    clear()
    print_slow("\n- come on " + name + ", you can't die and leave me alone here!\n", Fore.BLUE)
    time.sleep(1)
    print_slow(
        "\nYou hear a voice far off in the distance calling\n" 
        "out to you and you begin to regain consciousness.\n")
    time.sleep(1)
    input(Fore.GREEN + "\nPress w to wake up: " )
    clear()
    print_slow(
        "\nSlowly you open your eyes and see your friend\n"
        "Oliwer leaning over you!\n\n"
        "You sit up slowly and your head aches.\n"
        "When you bring your hand to your head,\n" 
        "you feel a bump.\n")
    time.sleep(1)
    input(Fore.GREEN + "\nPress t to talk with Oliwer: " )
    clear()
    print_slow("\n- what happened? where are we?\n\n", Fore.YELLOW)
    print_slow(
        "- The boat sank. When I woke up I found you lying a few meters away.\n"
        "  I ran as fast as I could to give you first aid.\n"
        "  The waves seem to have driven us to"
        "  some sort of island.\n\n", Fore.BLUE
    )
    print_slow("Oliwer extends his hand to help you up\n")
    input(Fore.GREEN+ "\nPress h to take Oliwers hand: " )
    
    
def the_shelter():
    """
    The user most enter a choice.
    Each choice has different stories
    but both lead the user further in the game.
    Are the choice not valid an error message
    with instructions is displayed
    """
    clear()
    print_slow(
        "\n- What do you think " + name + ", should we try to build\n"
        "  a shelter here on the beach or should we\n"
        "  go further into the island to seek\n"
        "  shelter for the night?\n", Fore.BLUE)
    print()
    print(Fore.GREEN + "build or seek:\n")
    choice = input(Fore.YELLOW + ">> ")
    while choice not in ("build", "seek"):
        print(Fore.RED + "\nInvalid choice, you must choose build or seek!\n")
        choice = input(Fore.YELLOW + ">> ")
    if choice == "build":
        clear()
        print_slow(
                "\nYou and Oliwer start looking for driftwood\n"
                "that you can use to build a shelter.\n"
                "After an hour of searching you start to get hungry\n"
                "and realize that it is hopeless to find any driftwood.\n"
                "Finally you decide to go further into the island.\n"
                "You find edible berries and a cave\n"
                "where you seek shelter for the night\n")
    elif choice == "seek":
        print_slow("")
   
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
    the_stranded_friends()
    the_shelter()
    chapter_4()
    chapter_5()
    end_scen_1()
    end_scen_2()
    


main()
