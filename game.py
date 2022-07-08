import random
answer = random.randint(1,10)
counts=3
while counts>0:
    guess = int(input("number:"))

    if guess == answer:
        print("right")
        break
    else:
        if guess <answer:
            print("small")
        else:
            print("big")
        counts= counts -1    
print("game is over")
