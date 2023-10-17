print("Math Game\n")
a = 0
b = ""
while b != "yes":
  multiples = int(input("\nName your multiples: "))
  for i in range (1,11):
    answer = int(input(f'{multiples} x {i} = '))
    if answer == (i*multiples):
      print("Great work!\n")
      a += 1
    else:
      print("The answer is",(i*multiples),"\n")
  if a == 10:
    print("Amazing! Perfect score! 10 out of 10 \n")
  else:
    print(f"Great job!, you get {a} out of 10 \n")
  b = input("Would you like to exit? ")
  a = 0
exit()
