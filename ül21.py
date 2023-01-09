import random

x =random.randint(1, 101)

guess = -1

while x != guess:

    guess = int(input("paku arvu: "))

    if x > guess:
        print('Paku suurem')
    elif x < guess:
        print('paku väiksem')
    elif x == guess:
        print('õige!')

    print(x == guess)
    
