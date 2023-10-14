adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer =  myBill / numberOfPeople
print("You all owe", round(answer, 2))
print()
print ("Tip Calculator")
print()
bill = float(input("How much did you spend?: "))
tip = int(input("What percentage do you want to tip?: "))
people = int(input("How many people in you group?: "))
answer = (bill/100*tip+bill)/3
print()
print ("You each owe",round(answer, 2))
print ("You each owe £"+ str(round(answer, 2)))