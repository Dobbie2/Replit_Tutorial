def rollDice():
    print("Infinity Decice 🎲")
    print()
    sides = int(input("How many sides does the dice have?: "))
    while True:
        import random
        dice = random.randint(1, sides)
        print()
        print("You rolled",dice)
        print()
        again = input("\33[31mRoll again?: \33[97m")
        if again == "y":
            continue
        else:
            break

rollDice()