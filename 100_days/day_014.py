from getpass import getpass as input

print("Let's play Rock, Paper, Scissors!\n" )
print("Select your move (R, P or S)\n")

p1 = input("Player1 >" )
p2 = input("Player2 >" )

if p1=="R":
  if p2=="R":
    print("Draw!" )
  elif p2=="S":
    print("Player1 used Rock! It was super effective! Player2's Scissors broke." )
  elif p2=="P":
    print("Player2 used Paper! It was super effective! Player1's Rock is smothered." )
  else:
    print("Player2, please use capital R/P/S." )
elif p1=="P":
  if p2=="R":
    print("Player1 used Paper! It was super effective! Player2's Rock is smothered.")
  elif p2=="S":
    print("Player2 used Scissors! It was super effective! Player1's Paper is chopped up." )
  elif p2=="P":
    print("Draw!" )
  else:
    print("Player2, please use capital R/P/S." )
elif p1=="S":
  if p2=="R":
    print("Player2 used Rock! It was super effective! Player1's Scissors broke." )
  elif p2=="S":
    print("Draw!" )
  elif p2=="P":
    print("Player1 used Scissors! It was super effective! Player2's Paper is chopped up." )
  else:
    print("Player2, please use capital R/P/S." )
else:
  print("Player1, please use capital R/P/S." )