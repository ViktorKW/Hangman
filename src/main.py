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


import os
from random import randint


file = open("words.txt", "r")
words_list = []


for word in file:
    words_list.append(word)


while True:
    os.system('clear')
    print("HANGMAN begins!\n")


    mystery_word = words_list[randint(0, len(words_list))]


    is_revealed = [False]*(len(mystery_word)-1)


    def reveal_random(mystery_word, is_revealed):
        letter = randint(0, len(mystery_word)-2)
        if is_revealed[i]:
            reveal_random(mystery_word, is_revealed)
        else:
            is_revealed[letter] = True


    for i in range(int(len(mystery_word)/4)):
        reveal_random(mystery_word, is_revealed)


    print(mystery_word)
    for i in range(len(is_revealed)):
        if is_revealed[i]:
            print(mystery_word[i], end = "")
        else:
            print("-", end ="")
#    print(player_word)
#    print(len(player_word))


    strikes = 0


    #while strikes <= 5:
    #    print(hangman[strikes])
    #    strikes+=1
    #    input()
    input()
    break
