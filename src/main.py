import os
from game_manager import *


while True:
    os.system('clear')
    print("HANGMAN begins!\n")
    g = game_manager()

    print("Wanna try again?")
    print("Press 'Enter' for another round!")
    if input() == "\n":
        continue
    else:
        break
        
print("Thanks for playing! :D")
