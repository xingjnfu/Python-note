import random   “”“引入一个random，可以使用随机生成数”“”
answer = random.randint(1,10)     “”“random.randint(a,b)a,b代表范围”“”
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
