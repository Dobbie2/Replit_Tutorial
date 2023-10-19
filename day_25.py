#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin
    
myPin = pinPicker(4) #4 means we want 4 random numbers
print(myPin)

def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area
area = areaOfTriangle (5, 22)
print(area)

def area_square(side1, side2):
  area = side1 * side2
  return area

area = area_square(4, 12)
print(area)

def dice(number6,number8):
    import random
    score = int(random.randint(1,number6)) * int(random.randint(1,number8))
    return score
    
print("\033[94m🛡  Character Stats Generator 🗡️\033[0m")
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