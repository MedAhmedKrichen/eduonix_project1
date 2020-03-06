import random


games=int(input("give the number of games you wanna to play"))
for i in range(games):
    target = random.randint(1, 25)
    k=0
    s = int(input("give a random  number between 1-25"))

    while s not in(range(1,26)):
            s=int(input("give a random  number between 1-25"))
    while s != target:
        if s>target :
            print("the number is higher")
            k+=1
            s = int(input("give a random  number between 1-25"))
            while s not in (range(1, 26)):
                s = int(input("give a random  number between 1-25"))
        elif s < target:
            print("the number is lower")
            k +=1
            s = int(input("give a random  number between 1-25"))
            while s not in (range(1, 26)):
                s = int(input("give a random  number between 1-25"))
    else :
        k +=1
        print("you guess it right after %d"%k)
