# This challenge is the same as day 18 because import random was taught early.

import random as r

print("===Guess the Number===")

my_number = r.randint(1,1_000_000)

counter = 0
# I chose to print the number in this demonstration to ensure 
# that the counter was working properly. 
# This would be removed before deployment if it were an official program.
print(my_number)
while True:
  guess = int(input("Gimme a number between 1 and 1,000,000. "))

  if my_number == guess:
    print("Hey, you got it!")
    counter +=1
    break
  elif guess < my_number:
    print("Too low! \n")
    counter +=1
  elif guess > my_number:
    print("Too high! \n")
    counter +=1
  else:
    print("Input not recognized. ")

print(f"It took you {counter} tries!")