print("Exam Grade Calculator")
print()
nameExam = input("What was the name of the exam?: ")
max = int(input("What was the maximum possible score?: "))
yourScore = int(input("What was your score?: "))

score = round(yourScore/max*100,2)
final = str(score)

print()
print("You scored", final+"% for the",nameExam, "exam")
print()
if score >= 90:
  print ("Your letter grade is A+ 😃")
elif score <= 89 and score >=80:
  print ("Your letter grade is A 😄")
elif score <= 79 and score >=70:
  print ("Your letter grade is B 😀")
elif score <= 69 and score >=60:
  print ("Your letter grade is C 😏")
elif score <= 59 and score >=50:
  print ("Your letter grade is D 😗")
else:
  print ("Your letter grade is U 😟")