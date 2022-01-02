from hangman import *
from letter_table import *


class game_manager():
    def __init__(self):
        self.hangman = hangman()
        self.letter_table = letter_table()
        self.letter_table.print_table()
        self.strikes = 0
    def __game_cycle(self):
        while self.strikes < 5:
