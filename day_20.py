# count from 0 to 100 in steps of 5
for counter in range(0,101,5):
  print("For counter",counter)
#count from 100 to 109
for i in range(100, 110):
  print(i)
# count from 1 to 6
for i in range(1, 7):
  print("Day", i)
# count from 1 to 7
for i in range(1, 8):
  print("Day", i)
# prints 13 times table
print("Thirteen Times Table")
for i in range(1, 13):
  print(i, "x 13 =", i * 13)
# counts in steps of 25
  for i in range (0, 1000000, 25):
    print(i)
# counts down drom 0 to -9
for i in range(0, -10, -1):
  print(i)

  for i in range (10, 0,-1):
    print(i)

for i in range (40, 20, -1):
  print(i)

print("List Genaerator")
print()
  
s = int(input("Start at: "))
e = int(input("End before: "))
i = int(input("Increment betwee values: "))
for i in range(s,e,i):
  print(i)