import string
from bcolors import *

class letter_table():
    def __init__(self):
        self.table = list(string.ascii_lowercase)
        self.is_tagged = [False]*(len(self.table))


    def print_table(self):
        for i in range(len(self.is_tagged)):
            if self.is_tagged[i]:
                print(bcolors.OKBLUE + self.table[i] + bcolors.ENDC, end="\t")
            else:
                print(bcolors.WARNING + self.table[i] + bcolors.ENDC, end="\t")
        print(" ", end = "\n")
