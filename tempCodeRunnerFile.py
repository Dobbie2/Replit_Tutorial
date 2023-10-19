def dice(number6,number8):
    import random
    score = int(random.randint(1,number6)) * int(random.randint(1,number8))
    return score
    

print(" \033[94m🛡  Character Stats Generator ⚔\033[0m")
print()
print("Type exit to leave the generator")
print()
while True:
  
  finalScore = dice(6,8)
  name =input("Name your warrior> ")
  if name == "exit":
     break
  elif finalScore >= 24:
    print ("redTheir health is",finalScore+"hp")
    print()
     
  else:
    print ("Their health is",finalScore,"hp")
    print()