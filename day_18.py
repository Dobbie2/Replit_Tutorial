
import random

number = (random.randint(0,100))
count = 1
while True:
    print()
    guess = int(input("What is your guess?: "))
    if guess < 0:
        print("\33[93mFail!! your guess of",guess, "is not between 0 and",number)
        exit()
    elif guess == number:
        break
    elif guess > number:
        count += 1
        print("\33[31mToo high \33[97m")
    elif guess < number:
        count += 1
        print("\33[94mToo low \33[97m")
print()
print ("\33[92mSpot on!\33[97m")
print("You completed the gaame with",count,"attempts")
print()
