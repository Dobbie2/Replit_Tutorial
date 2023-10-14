print(" Wholesome Positivity Machine")
print()

name = input("What is your name?: ")
achieve = input("What do you want to achieve?: ")
feel = int(input("On ascale of 1 to 10 how do you feel today?: "))
if name == "Dobbie" and feel <= 5:
    print("Hey", name,"Keep your chin up! Today you're going to", achieve+"! in the most amazing way, simple by being you - YOU ROCK")

elif name == "Dobbie" and feel >= 6:
    print("Hey", name,"My you are on a high! Today you're going to", achieve+"! in the most amazing way, simple by being you - YOU ROCK")

elif name == "Scallie" and feel <= 5:
    print("Hey", name,"Keep your chin up! Today you're going to", achieve+"! in the most amazing way, simple by being you - YOU ROCK")

elif name == "Scallie" and feel >= 6:
    print("Hey", name,"My you are on a high! Today you're going to", achieve+"! in the most amazing way, simple by being you - YOU ROCK")

else:
    print("Sorry", name, "I don't know that name!")