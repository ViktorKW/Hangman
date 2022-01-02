import string
from bcolors import *

class letter_table():
    def __init__(self):
        self.table = list(string.ascii_lowercase)
        self.tagged_letters = [False]*(len(self.table))
        

    def print_table(self):
        for i in range(len(self.tagged_letters)):
            if self.tagged_letters[i]:
                print(bcolors.OKBLUE + self.table[i] + bcolors.ENDC, end="\t")
            else:
                print(bcolors.WARNING + self.table[i] + bcolors.ENDC, end="\t")
