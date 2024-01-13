import sys
import os
import pyfiglet 
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

result = pyfiglet.figlet_format("The Lost Island", font="block" ) 
print(result) 