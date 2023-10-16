number = (79)

guess = int(input("What is your guess?: "))

while True:
    guess = int(input("What is your guess?: "))
    if guess == number:
        break
    elif guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    #else:
        #break
print ("end")
