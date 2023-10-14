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
print("Well done! It only took you",count, "attempts.")
              