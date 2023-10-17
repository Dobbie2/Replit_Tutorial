import random

for i in range(1,11):
    myNumber = random.randint(1,100)
    print(myNumber)

import random

myNumber = random.randint(1, 100)
print(myNumber)

import random


for i in range(10):
  myNumber = random.randint(1, 100)
  print(myNumber)

import random
print("\33[92mGuess the number game")
print()
print("Number will be between 0 and 100\33[97m")
print()
while True:
    number = (random.randint(0,100))
    count = 1
    while True:
        print()
        guess = int(input("What is your guess?: "))
        if guess == number:
            print()
            print ("\33[92mSpot on!")
            print("It took you",count,"guesses to get the radom number correct!\33[97m")
            print()
            again = input("Do you want play again? Y/N ")
            if again.lower() == "y":
                break
            else:
                exit()
        
        elif guess < 0:
            print("\33[93mFail!! your guess of",guess, "is not between 0 and",number)
            exit()
        elif guess > number:
            count += 1
            print("\33[31mToo high \33[97m")
        elif guess < number:
            count += 1
            print("\33[94mToo low \33[97m")
 
