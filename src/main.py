hangman = ["""
 O
-|-
/ \\\n
""",
"""
  O
 -|-
 / \\
^^^^^
|||||\n
""",
"""
|
|
|      O
|     -|-
|     / \\
|    ^^^^^
|    |||||\n
""",
"""
|-------
|
|      O
|     -|-
|     / \\
|    ^^^^^
|    |||||\n
""",
"""
|-------
|      |
|      O
|     -|-
|     / \\
|    ^^^^^
|    |||||\n
""",
"""
|-------
|      |
|      O     HANGMAN
|     -|-    IS DEAD
|     / \\
|
|\n
"""

]





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
    #---game init end
    print("HANGMAN begins!\n")
    strikes = 0

    while strikes <= 5:
        print(hangman[strikes])
        strikes+=1
        input()

    input()
    break
