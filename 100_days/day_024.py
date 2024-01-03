import random as r

again = "yes"

while again == "yes":
  def dice():
    dice = int(input("How many sides to your die? "))
    dice = r.randint(1, dice)
    return dice
  
  print("You rolled", dice())
  again = input("Wanna roll again? ")