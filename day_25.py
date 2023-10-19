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