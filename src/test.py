#i = int(6/7)
#
#print(i)
#
from random import randint
#
#print(randint(1,5))


#def func(mystery):
#    print("should change")
#    mystery = 50

#num = 40
#print(num)
#func(&num)
#print(num)

def reveal_random(mystery_word, is_revealed):
    letter = int(randint(0, len(mystery_word)-1))
    if is_revealed[i]:
        reveal_random(mystery_word, is_revealed)
    else:
        is_revealed[letter] = True



mystery_word = "volosomonosov"

is_revealed = [False]*len(mystery_word)

for i in range(int(len(mystery_word)/4)):
    reveal_random(mystery_word, is_revealed)

print(is_revealed)
