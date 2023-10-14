while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I was having a good time 😭")
print()
print()



counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")
print()
print()


while True:
  colour = input("Enter a color: ")
  if colour == "red":
    break
  else:
    print(colour,"is a cool color!")
print("I don't like red")
print()
print()


print("Fill in the blank lyrics!")
print("(Type in the blank lyrics and see if you are as cool as me.)")
print()

count = 1
print ("Never going to ______ you up")
print()
while True:
    lyrics = input(" what is the missing lyrics?: ")
    if lyrics != "give":
        print("Nope, try again")
        count +=1
    elif lyrics == "give":
        break
if count == 1:
    print("Well done! It only took you",count, "attempt.")
else:
    print("Well done! It only took you",count, "attempts.")