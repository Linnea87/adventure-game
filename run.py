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
    
def restart():
    """ Restarts the game"""
    python = sys.executable
    os.execl(python, python, * sys.argv)



def welcome():
    """
    Welcomes the user to the game and ask if the user
    have the courage to play.
    """
    clear()
    print_slow("\n\t\t\t\t  Welcome to\n\n")
    time.sleep(1)
    """ ASCII art """
    result = pyfiglet.figlet_format(
        "The Lost Island", font="cybermedium", justify="center")
    print(Fore.CYAN + result)
    print_slow("\t\tDo you have the courage to enter this adventure?\n\n")
    time.sleep(1)
    print(Fore.GREEN + "  yes or no?\n")


def player_answer():
    """
    Prompt the user to enter a answer.
    Different messages are displayed depending
    on the user's answer
    Is the users answer not valid, an error message
    with instructions is displayed
    """
    answer = input(Fore.YELLOW + "  >> ").lower()
    while answer not in ("yes", "no"):
        print(Fore.RED + "\n  Invalid answer, enter yes or no!\n")
        answer = input(Fore.YELLOW + "  >> ").lower()
    if answer == "no":
        print_slow("\n\tOh, that's to bad! Maybe another time then :)\n\n")
        time.sleep(1)
        clear()
        restart()
    elif answer == "yes":
        clear()
        print_slow(
            "\n\tGood! The first thing you have to do "
            "is enter your name below!\n\n"
        )


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
            name = input(Fore.YELLOW + "  >> ")
            if not name.isalpha():
                print(Fore.RED + "\n  Your name can only contain letters!\n")
            elif len(name) < 3:
                print(
                    Fore.RED + "\n  Your name needs to be 3 letters or more!\n")
            else:
                print_slow(
                    "\n\t" + name + ", you are now about to begin perhaps\n"
                    "\tyour most exciting, fast-paced and dangerous\n"
                    "\tadventure you have ever been on!\n\n"
                )
                input(
                    Fore.GREEN + "  So when you feel ready to begin just "
                    "hit enter! "
                )
                break
        except Exception as e:
            print(Fore.RED + f" An error occurred: {e}")


def intro():
    """
    The adventure game starts with an exciting intro
    using the print_slow function
    """
    clear()
    print_slow(
        "\n\t\tWhat was supposed to be a quiet and\n"
        "\t\tlovely boating holiday out at sea\n"
        "\t\twith some of your closest friends,\n"
        "\t\tturned out to be the complete opposite!\n\n"
        "\t\tAfter a few days, you end up in the eye\n"
        "\t\tof the worst storm you've ever experienced.\n"
        "\t\tThe heavy rain and the powerful waves\n"
        "\t\tdestroy parts of your boat and it slowly\n"
        "\t\tbegins to sink.\n\n"
        "\t\tIn a panic, you try to get to\n"
        "\t\tthe lifeboat to save you and your friends,\n"
        "\t\twhen suddenly you collapse and\n"
        "\t\teverything goes dark!\n"
    )
    time.sleep(1)


def the_stranded_friends():
    """
    With help of the input function, the user must
    interact so that the story progresses.
    """
    clear()
    print_slow(
        "\n\t\t- Come on " + name + "! You can't die and\n"
        "\t\t  leave me alone here!\n", Fore.BLUE
    )
    time.sleep(1)
    print_slow(
        "\n\tYou hear a voice far off in the distance calling\n"
        "\tout to you and you begin to regain consciousness.\n\n"
    )
    time.sleep(1)
    input(Fore.GREEN + "  Press enter to wake up! ")
    print_slow(
        "\n\tSlowly you open your eyes and see your\n"
        "\tfriend Oliwer leaning over you!\n\n"
        "\tYou sit up slowly and your head aches.\n"
        "\tWhen you bring your hand to your head,\n"
        "\tyou feel a bump.\n\n"
    )
    time.sleep(1)
    input(Fore.GREEN + "  Press enter to talk with Oliwer! ")
    clear()
    print_slow("\n\t\t- what happened? where are we?\n\n", Fore.YELLOW)
    print_slow(
        "\t\t- The boat sank. When I woke up I\n"
        "\t\t  found you lying a few meters away.\n"
        "\t\t  I ran as fast as I could to give you first aid.\n"
        "\t\t  The waves seems to have driven us to some\n"
        "\t\t  sort of island.\n\n", Fore.BLUE
    )
    print_slow("\tOliwer extends his hand to help you up.\n")
    input(Fore.GREEN + "\n  Press enter to take Oliwers hand! ")


def the_shelter():
    """
    The user most enter a choice.
    Each choice leads to different outputs in the game.
    Are the choice not valid an error message
    with instructions is displayed
    """
    clear()
    print_slow(
        "\n\t\t- What do you think " + name + ", should we try to build\n"
        "\t\t  a shelter here on the beach or should we\n"
        "\t\t  go further into the island to seek\n"
        "\t\t  shelter for the night?\n\n", Fore.BLUE
    )
    print(Fore.GREEN + "  build or seek?\n")
    choice = input(Fore.YELLOW + "  >> ").lower()
    while choice not in ("build", "seek"):
        print(
            Fore.RED + "\n  Invalid choice, you must choose build or seek!\n"
        )
        choice = input(Fore.YELLOW + "  >> ").lower()
    if choice == "build":
        return the_beach()
    elif choice == "seek":
        return the_winding_path()


def the_beach():
    """
    One of the paths with an interactive story and
    the game continues
    """
    clear()
    print_slow(
        "\n\tYou and Oliwer start looking for driftwood\n"
        "\tthat you can use to build a shelter.\n\n")
    print_slow(
        "\t\t- " + name + " come quickly and see what I found!\n\n", Fore.BLUE)
    input(Fore.GREEN + "  press enter to run to Oliwer: ")
    print_slow(
        "\n\tThere in the water it floats around the\n"
        "\tmost beautiful driftwood you've ever seen!\n\n")
    input(Fore.GREEN + "  Press enter to wade into the water! ")
    print_slow(
        "\n\tAfter what feels like an eternity, you have managed\n"
        "\tto collect the driftwood that was floating around,\n"
        "\tand built your shelter for the night.\n"
    )
    time.sleep(1)


def the_winding_path():
    """
   This path gives the user an interactive story
   and the game continues
    """
    clear()
    print_slow(
        "\n\tYou and Oliwer start walking further into\n"
        "\tthe island and end up on a winding path.\n"
        "\tAfter what feels like an eternity, you have\n"
        "\tfinally managed to fight your way out\n\n"
    )
    print_slow("\t\t - " + name + " look!\n\n", Fore.BLUE)
    input(Fore.GREEN + "  Press enter to look where Oliwer is pointing! ")
    print_slow(
        "\n\tThere are plants of all kinds and colors.\n"
        "\tAnd lots of different kinds of berries.\n\n"
    )
    input(Fore.GREEN + "  press enter to pick berries! ")
    print_slow(
        "\n\tWhen you have picked your pockets full of\n"
        "\tedible berries, it has started to get dark.\n"
        "\tYou are forced to seek shelter under a\n"
        "\tlarge tree for the night.\n"
        "\tYou satisfy part of your hunger with the\n"
        "\tberries you managed to bring with you.\n"
    )
    time.sleep(1)


def the_serch_for_water():
    """
    The user must make a decision. Is the decision
    not valid, an error message is displayed and the user gets
    a second chance to make a decision.
    """
    clear()
    print_slow(
        "\n\t\t- " + name + " our drinking water has run out!\n\n", Fore.BLUE)
    time.sleep(1)
    print_slow(
        "\tAfter days without rain, you start\n"
        "\tlooking for sources of potable water.\n\n"
        "\tWhen you have hiked for half the day,\n"
        "\tyou will arrive at a mountain cave.\n\n"
    )
    time.sleep(1)
    print_slow(
        "\n\t\t- Do we really have to go in there " + name + "?\n"
        "\t\t  It's jet black.\n"
        "\t\t  Isn't it better to try to walk\n"
        "\t\t  around the cave instead?\n\n", Fore.BLUE
    )
    time.sleep(1)
    print(Fore.GREEN + "  go in or go around?\n")
    userInput = input(Fore.YELLOW + "  >> ").lower()
    while userInput not in ("go in", "go around"):
        print(Fore.RED + "\n  Invalid answer, enter go in or go around\n")
        userInput = input(Fore.YELLOW + "  >> ").lower()
    if userInput == "go in":
        return mountain_cave()
    elif userInput == "go around":
        return the_field()


def mountain_cave():
    """
    This interactive story
    leads the user further in the game
    """
    clear()
    print_slow(
        "\n\tYou enter the cave and after a while\n"
        "\tyour eyes start to get used to the darkness\n"
        "\tYou walk along the cave walls to move forward.\n\n"
    )
    time.sleep(1)
    print_slow("\t\t- What is that sound?\n\n", Fore.BLUE)
    time.sleep(1)
    print_slow("\t\t- I don't know, let's follow it!\n\n", Fore.YELLOW)
    input(Fore.GREEN + "  Press enter to follow the sound! ")
    print_slow(
        "\n\tYou begin to approach where the sound is\n"
        "\tcoming from and you glimpse daylight.\n"
        "\tYou follow the light and come to a spring\n"
        "\tfull of drinkable rainwater.\n\n"
    )
    print_slow(
        "\tYou run forward and start drinking\n"
        "\tas much as you can handle.\n"
        "\tWhen you are no longer thirsty, you\n"
        "\tlook for something to refill your\n"
        "\twater with without any luck.\n\n"
    )
    print_slow(
        "\tYou therefore decide to find a\n"
        "\tgood place outside the cave\n"
        "\tto build a new camp.\n"
    )
    time.sleep(1)


def the_field():
    """
    Here the interactive story leads the
    user to their death and the game ends
    """
    clear()
    print_slow(
        "\n\tYou go around the mountain cave\n"
        "\tand find another way.\n\n"
        "\tThe sun is scorching and\n"
        "\tafter hours of hiking\n"
        "\tyou are so tired and\n"
        "\tdehydrated that you\n"
        "\tdon't notice that you have ended up\n"
        "\tin the middle of a field of quicksand.\n\n"
    )
    print_slow("\t\t- Help, I'm sinking!!!!\n\n", Fore.BLUE)
    time.sleep(1)
    input(Fore.GREEN + "  Press enter to help Oliwer! ")
    clear()
    print_slow(
        "\n\tYou run to Oliwer, but you are so tired\n"
        "\tand have no energy left,\n"
        "\tthat you stumble right into the quicksand.\n"
        "\tAnd neither you nor Oliwer survive.\n\n"
    )
    print(Fore.CYAN + "  ****************************"
          "***********************\n")
    input(Fore.GREEN + "  press enter to try again! ")
    restart()


def mountain_top():
    """
    
    """
    clear()
    print_slow(
        "\n\tSeveral weeks have passed since you found the\n"
        "\tmountain cave. You've set off to look for\n"
        "\tedibles as the food you've collected starts\n"
        "\tto wear out.\n\n"
    )
    print_slow(
        "\t\t- " + name + " do you see what "
        "i see over there?\n\n", Fore.BLUE
    )
    input(Fore.GREEN + "  Press enter to answer Oliwer! ")
    print_slow("\n\t\t- Yes I see, it's the top of a mountain!\n", Fore.YELLOW)
    time.sleep(1)
    print_slow(
        "\n\tEagerly, you start walking towards the mountain top.\n"
        "\tAfter you have hiked for a few hours, the path splits\n"
        "\tand the trees obscure the view of the mountain top.\n\n"
    )
    print(Fore.GREEN + "  right or left?\n")
    path = input("  >> ").lower()
    while path not in ("right", "left"):
        print(Fore.RED + "\n  Invalid answer, choose right or left\n")
        path = input("  >> ").lower()
    if path == "right":
        return the_rickety_bridge()
    elif path == "left":
        return the_waterfall()


def the_rickety_bridge():
    clear()
    print_slow(
        "\tA bit into the path you will come to a\n"
        "\trickety bridge, and under the bridge there\n"
        "\tis a precipice. You quickly notice that there\n"
        "\tis no other way but to cross the bridge.\n\n"
    )
    print_slow(
        "\tWhen you get to the middle of the bridge,\n"
        "\tyou notice that several planks are missing,\n"
        "\tand you have to jump over the big hole to\n"
        "\tget to the other side of the bridge.\n\n"
    )
    print_slow("\t\t- I jump first Oliwer!\n\n", Fore.YELLOW)
    input(Fore.GREEN + "  Press enter to jump: ")
    print_slow(
        "\n\tWhen you start to jump, the bridge collapses\n"
        "\tand you both fall into the abyss and do not survive.\n\n"
    )
    print(Fore.CYAN + "  ****************************"
          "***********************\n")
    input(Fore.GREEN + "  press enter to try again! ")
    restart()


def the_waterfall():
    clear()
    print_slow(
        "\n\tA little further into the path\n"
        "\tyou will come to a large waterfall.\n\n"
    )
    print_slow(
        "\t\t- " + name + " Let's jump in and cool off!\n\n", Fore.BLUE)
    input(Fore.GREEN + "  Press enter to take a cooling bath: ")
    print_slow(
        "\n\tWhen you have finished swimming, you continue\n"
        "\tyour hike towards the top of the mountain.\n\n"
        "\tAt dusk you have finally arrived at a high mountain.\n"
        "\tYou choose to camp here for the night.\n"
    )


def the_rescue():
    clear()
    print_slow(
        "\n\t\t- " + name + " wake up wake up!!\n\n", Fore.BLUE)
    print_slow(
        "\tYou wake up with a jolt and hear the\n"
        "\tmuffled sound of a helicopter.\n"
        "\thurriedly you start looking around to find\n"
        "\tdifferent ways to get up the mountain.\n\n"
        "\tA little way off you see a path\n"
        "\twinding through the mountain.\n\n"
    )
    print_slow(
        "\t\t- Should we take the fast track and climb\n"
        "\t\t  the mountain or should we take the path\n"
        "\t\t  through the mountain?\n\n", Fore.BLUE
    )
    time.sleep(1)
    print(Fore.GREEN + "  path or climb?\n\n")
    the_last_choice = input(Fore.YELLOW + "  >> ").lower()
    while the_last_choice not in ("path", "climb"):
        print(Fore.RED + "\n  Invalid answer, enter path or climb\n")
        the_last_choice = input(Fore.YELLOW + "  >> ").lower()
    if the_last_choice == "path":
        return through_the_mountain()
    elif the_last_choice == "climb":
        return the_climb()


def through_the_mountain():
    clear()
    print_slow(
        "\n\tYou run as fast as you can up\n"
        "\tthe winding path. You are tired but\n"
        "\tmanage to get to the top. You\n\n"
        "\ttake off your shirts and start waving\n"
        "\tthem with all the strength you have left.\n"
        "\tYou see the helicopter turning and landing.\n\n"
    )
    input(Fore.GREEN + "  Press enter to go to the helicopter\n! ")
    print_slow(
        "\tYou get into the helicopter that takes you home\n"
        "\tafter several weeks of survival on the island!\n"
    )
    print(Fore.CYAN + "  ****************************"
          "***********************\n")
    input(Fore.GREEN + "  press enter to try again! ")
    restart()


def the_climb():
    clear()
    print_slow(
        "\n\tYou start climbing up the mountain.\n"
        "\tHalfway up, fatigue starts to set in\n"
        "\tand you get lactic acid in both your legs and arms.\n\n"
        "\tOliwer, who climbs first, loses his grip and falls.\n\n"
    )
    time.sleep(1)
    input(Fore.GREEN + "  Press enter to save Oliver! ")
    print_slow(
        "\n\tYou reach to try to grab Oliver's hand,\n"
        "\tbut you lose your grip with your other hand and fall.\n"
        "\tYou hear how the sound of the helicopter\n"
        "\tdisappears into the distance, and everything\n"
        "\tbecomes black and empty.\n\n"
    )
    print(Fore.CYAN + "  ****************************"
          "***********************\n")
    input(Fore.GREEN + "  press enter to try again! ")
    restart()


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
    the_serch_for_water()
    mountain_top()
    the_rescue()


main()
