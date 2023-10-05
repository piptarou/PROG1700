from getpass import getpass as input

p1_counter = 0
p2_counter = 0

print("Let's play Rock, Paper, Scissors!\n" )
print("Select your move (R, P or S)\n")

while True:
  p1 = input("Player1 >" )
  p2 = input("Player2 >" )

  if p1=="R":
    if p2=="R":
      print("Draw!\n" )
    elif p2=="S":
      print("Player1 used Rock! It was super effective! Player2's Scissors broke.\n" )
      p1_counter += 1
    elif p2=="P":
      print("Player2 used Paper! It was super effective! Player1's Rock is smothered.\n" )
      p2_counter += 1
    else:
      print("Player2, please use capital R/P/S.\n" )
  elif p1=="P":
    if p2=="R":
      print("Player1 used Paper! It was super effective! Player2's Rock is smothered.\n")
      p1_counter += 1
    elif p2=="S":
      print("Player2 used Scissors! It was super effective! Player1's Paper is chopped up.\n" )
      p2_counter += 1
    elif p2=="P":
      print("Draw!\n" )
    else:
      print("Player2, please use capital R/P/S.\n" )
  elif p1=="S":
    if p2=="R":
      print("Player2 used Rock! It was super effective! Player1's Scissors broke.\n" )
      p2_counter += 1
    elif p2=="S":
      print("Draw!\n" )
    elif p2=="P":
      print("Player1 used Scissors! It was super effective! Player2's Paper is chopped up.\n" )
      p1_counter += 1
    else:
      print("Player2, please use capital R/P/S.\n" )
  else:
    print("Player1, please use capital R/P/S.\n" )

  print("Player 1 has", p1_counter, "wins.")
  print("Player 2 has", p2_counter, "wins.\n")
  
  if p1_counter==3 or p2_counter==3:
    print("Thanks for playing!")
    exit()
  else:
    continue