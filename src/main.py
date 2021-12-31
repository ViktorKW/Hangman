from random import randint


file = open("words.txt", "r")
words_list = []


for word in file:
    words_list.append(word)


mystery_word = words_list[randint(0, len(words_list))]

import os
from random import randint


file = open("words.txt", "r")
words_list = []


for word in file:
    words_list.append(word)


while True:
    #---game init
    os.system('clear')
    mystery_word = words_list[randint(0, len(words_list))]
    
    hangman = """
     O
    -|-
    / \\\n
    """
    #---game init end
    print("HANGMAN begins!\n")
    print(hangman)
    input()
    break
