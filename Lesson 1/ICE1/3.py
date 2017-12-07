
from random import randint
nu = randint(0,9)
while True:
    s = input("\n Guess the digit: ")
    if s==nu:
        print("Your answer is PERFECT!!(Congratulations!!)")
        break
    elif s > nu:
        print("Your answer is high than requierd")
    else:
        print ("You answer is low than required")

