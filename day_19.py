counter = 0
while counter < 10:
  print("While counter",counter)
  counter += 1
print()
for counter in range(10):
  print("For counter",counter)
print()
for counter in range(50,61):
  print("For counter",counter)
print()
total = 0
for number in range (100):
  total += number
  print(total)

total = 10
for counter in range (100):
  total += 10
  print("total")
print()

print("Loan Interest Calculator")
print()
loan = int(input("How much do you want to borrow?: "))
rate =int(input("What will be the APR rate?: "))
years =int(input("How many years will the loan rub for?: "))
print()
for counter in range (years):
  loan += loan*(rate/100)
  total = str(round(loan,2))
  print ("Year",counter + 1,"£"+total)
print()
