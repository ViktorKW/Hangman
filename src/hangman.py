import string
from random import randint


class hangman():
    def __get_mystery_word(self):
        file = open("words.txt", "r")
        words_list = []

        for word in file:
            words_list.append(word)

        return words_list[randint(0, len(words_list))]


    def __init__(self):
        self.mystery_word = self.__get_mystery_word()
        self.is_revealed = [False]*(len(self.mystery_word)-1)
        self.strikes = 0
