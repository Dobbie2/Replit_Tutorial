import random, os, time


def rollDice(side):
    result = random.randint(1,side)
    return result

def health():
    healthStat = ((rollDice(6)* rollDice(12)/2)+10)
    return healthStat

def strength():
    strengthStat = ((rollDice(6)* rollDice(8)/2)+12)
    return strengthStat

while True:
    print("\033[94m⚔ Character Builder ⚔\033[0m")
    print()
    name = input("Name Your Legend:\n")
    print()
    character = input("Character Type (Human, Elf, Wiard, Orc,:\n" )
    print()
    print (name)
    print("HEALTH: ", health())
    print("STRENGTH: ", strength())
    print()
    print ("May your name go down in legend....")
    print()
    again = input("Again (y/n)\n")
    if again == "n":
        break
    time.sleep(1)
    os.system("clear")
    



