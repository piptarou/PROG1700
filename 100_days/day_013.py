print ("===Exam Grade Calculator===")
score: 100
grade = int(input("What score did you get? "))
if grade >=90 and grade <=100:
  print("You got an A+! Congrats!")
elif grade >=80 and grade <89:
  print("You got an A! Congrats!")
elif grade >=70 and grade <79:
  print("You got a B! Not too shabby!")
elif grade >=60 and grade <69:
  print("You got a C!")
elif grade >=50 and grade <59:
  print("You got a D, better luck next time!")
else:
  print("Aw man, you failed. Better luck next time.")