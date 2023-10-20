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
    print("\033[94m⚔ BATTLE TIMES ⚔\033[0m")
    print()
    c1Name = input("Name Your Legend:\n")
    print()
    c1Type = input("Character Type (Human, Elf, Wiard, Orc,:\n" )
    print()
    print (c1Name)
    c1Health = health()
    c1Strength = strength()
    print("HEALTH: ", c1Health)
    print("STRENGTH: ", c1Strength)
    print()
    print ("Who are they battling?")
    print()
    c2Name = input("Name Your Legend:\n")
    print()
    c2Type = input("Character Type (Human, Elf, Wiard, Orc,:\n" )
    print()
    print (c2Name)
    c2Health = health()
    c2Strength = strength()
    print("HEALTH: ", c2Health)
    print("STRENGTH: ", c2Strength)
    print()

    round = 1
    winner = None
   
    while True:
        time.sleep(1)
        os.system("clear")
        print("\033[94m⚔ BATTLE TIMES ⚔\033[0m")
        print()
        print("The battle begins!")

        c1Dice = rollDice(6)
        c2Dice = rollDice(6)

        difference = abs(c1Strength - c2Strength) + 1

        if c1Dice > c2Dice:
            c2Health -= difference
            if round == 1:
                print(c1Name, "Wins the first blow")
            else:
                print(c1Name, "Wins round", round)
        elif c1Dice > c2Dice:
            c1Health -= difference
            if round == 1:
                print(c2Name, "Wins the first blow")
            else:
                print(c2Name, "Wins round", round)
        else:
            print("Thier swords class and they draw round", round)
        print()
        print(c1Name)
        print("HEALTH: ", c1Health)
        print()
        print(c2Name)
        print("HEALTH: ", c2Health) 
        print()

        if c1Health <= 0:
            print(c1Name, "Has died!")
            winner = c2Name
        elif c2Health <= 0:
            print(c2Name, "Has died!")
            winner = c1Name
        else:
            print("They are both standing for the next round")
            round
            break

           

            





    again = input("Again (y/n)\n")
    if again == "n":
        break
    time.sleep(1)
    os.system("clear")
    



