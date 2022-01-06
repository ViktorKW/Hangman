import pdb
import os
from hangman import *
from letter_table import *
from sprites import *


class game_manager():
    def __init__(self):
        self.hangman = hangman()
        self.letter_table = letter_table()
        self.strikes = 0
        self.__game_cycle()

    def __loss(self):
        os.system("clear")
        print("THIS IS IT!\n")
        print(hangman_sprites[-1])  #prints hangman
        print("Mystery word was " + self.hangman.mystery_word)


    def __win(self):
        os.system("clear")
        print("THIS IS IT!\nYOU HAVE WON THE CONSOLE GAME!\n")
        print("Mystery word was indeed " + self.hangman.mystery_word)
        print("WELL DONE!")

    def __game_cycle(self):
        while self.strikes is not len(hangman_sprites)-1:

            os.system("clear")
            print(hangman_sprites[self.strikes])  #prints hangman
            
            print("\n")
            self.letter_table.print_table()  #prints alphabet
            print("\n")

            for i in range(len(self.hangman.mystery_word)):  #print mystery_word
                if self.hangman.is_revealed[i] == True:
                    print(self.hangman.mystery_word[i], end = "")
                else:
                    print("-", end="")
            print("")


            while True:
                userInput = input("Your input: ")
                userInput = userInput.lower()
                if len(userInput) == 1:
                    if userInput in self.letter_table.table:
                        if self.letter_table.is_tagged[self.letter_table.table.index(userInput)]:
                            print("You've already used that letter!")
                            continue
                        else:
                            self.letter_table.is_tagged[self.letter_table.table.index(userInput)] = True
                            break
                    else:
                        print ("Please enter valid character")
                        continue
                print ("Please enter only one character")


            guessInLower = userInput


            success = False
            for i in range(len(self.hangman.mystery_word)):
                if self.hangman.mystery_word[i] == guessInLower:
                    self.hangman.is_revealed[i] = True
                    success = True


            if success:
                if all(self.hangman.is_revealed):
                    self.__win()
                    break
            else:
                self.strikes += 1

        if self.strikes == len(hangman_sprites)-1:
            self.__loss()
