print("Maths Game!")
print()

m = int(input("Enter your mulyipes: "))
score = (0)
print()
for i in range(1,11):
    print(i,"X",m,"=")
    a = int(input("Enter your answer: "))
    if a == i*m:
        print("\33[92mGreat work 😀\33[97m")
        score +=1
        print()
    else:
        print("\33[31mNope, the answer was",i*m,"🥲\33[97m")
        print()
print()
print ("\33[94mYou scored",score,"out of 10\33[97m")
print()