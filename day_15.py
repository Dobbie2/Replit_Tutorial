counter = 0
while counter <= 100:
  print(counter)
  counter +=1
print ()
exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")
exit = ""
while exit != "yes":
  animal = input("What animal do you want?: ")
  if animal == "Cow":
    print("A", animal, "goes moo.")
  elif animal == ("Dog"):
      print("A", animal, "goes woof.")
  elif animal == ("Cat"):
    print("A", animal, "goes meow.")
  elif animal == ("Sheep"):
    print("A", animal, "goes baar.")
  exit = input("Exit?: ")

