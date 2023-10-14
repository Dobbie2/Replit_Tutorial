print("Check the number of second in a given year")
print()

year = int(input("What year would you like to check?: "))
rem = year%4
print()
if rem == 0:
    print(year,"Was a leap year so there are",60*60*24*366, "seconds in that year!")
    
    
else:
   print(year,"Was not leap year so there are",60*60*24*365, "\033[1;33;40m seconds in that year!") 
   print()
   #print ("\033[1;33;40m Yellow")
    # TODO: write code...