

def dice(number6,number8):
    import random
    score = int(random.randint(1,number6)) * int(random.randint(1,number8))
    return score
    

print("\033[94m🛡  Character Stats Generator ⚔️exit\033[0m")
print()
print("\33[33mType exit to leave the generator\33[97m")
print()
while True:
  
  finalScore = dice(6,8)
  name =input("Name your warrior> ")
  if name == "exit":
     break
  elif finalScore >= 24:
    print ("\33[31mTheir health is",finalScore,"hp\33[97m")
    print()
     
  else:
    print ("\33[32mTheir health is",finalScore,"hp\33[97m")
    print()