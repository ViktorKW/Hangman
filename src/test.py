#i = int(6/7)
#
#print(i)
#

#
#print(randint(1,5))


#def func(mystery):
#    print("should change")
#    mystery = 50

#num = 40
#print(num)
#func(&num)
#print(num)


from random import randint
import pdb



#def init_reveal(mystery_word, is_revealed):
#    letter = int(randint(0, len(mystery_word)-1))
#    if is_revealed[i]:
#        reveal_random(mystery_word, is_revealed)
#    else:
#        is_revealed[letter] = True



#mystery_word = "volosomonosov"
#pdb.set_trace()
#is_revealed = [False]*len(mystery_word)

#is_revealed[0] = True
#is_revealed[len(is_revealed)-2] = True

#print(is_revealed)

import string
mystery_word = "volos"
is_revealed = [False]*len(mystery_word)

print(len(is_revealed))
print(len(mystery_word))
print(is_revealed)
print(mystery_word)

alphabet = list(string.ascii_lowercase)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    STRIKEOUT = '\u0336'

print(bcolors.WARNING + "Warning: No active frommets remain. Continue?"+ bcolors.ENDC)
print(bcolors.WARNING + bcolors.STRIKEOUT+"Warning: No active frommets remain. Continue?"+ bcolors.STRIKEOUT+bcolors.ENDC)

print("Hhahhahha?")



buffer = list("zombie")
mystery_word = None
for i in range(len(buffer)):
    mystery_word.append(False,[buffer[i]])

print(buffer)
