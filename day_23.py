def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

for i in range(10):
    rollDice()

print("Replit Login System")
print()

def login():
    userName = input("What is your user Name > ")
    password = input("What is your password > ")
    print()
    print (userName,password)
    print()
    if userName != ("david") or password != ("baldies4life"):
        print("\33[31mWhoops! I don't recognize that username or password. Try again!\33[97m")
        print()
    else:
        print("\33[92mWelcome to Replit!")
        print()

login()