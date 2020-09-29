import random
x=random.randint(1, 20)
count=1
name=input("Please enter your name: ")
x1=int(input("Well,"+name+", I am thinking of a number between 1 and 20.\nTake a guess.\n"))
while (x!=x1) and(count!=3):
    if x1>x:
        print("That number is too high.")
    elif x1<x:
        print("That number is too low")
    x1=int(input("Take another guess.\n"))
    count+=1
if x1==x:
    print("Good job,", name,"You guessed my number in",count,"guesses!")
elif x1!=x:
    print("All",count,"of your guesses are wrong!.\nYOU LOST!!!")