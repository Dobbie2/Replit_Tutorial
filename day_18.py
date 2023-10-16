#number = (79)

import random

number = (random.randint(0,100))
count = 1
while True:
    print()
    guess = int(input("What is your guess?: "))
    if guess < 0:
        print("Fail!! your guess of",guess, "is not between 0 and",number)
        exit()
    elif guess == number:
        break
    elif guess > number:
        count += 1
        print("Too high")
    elif guess < number:
        count += 1
        print("Too low")
print()
print ("Spot on!")
print("You completed the gaame with",count,"attempts")
print()
