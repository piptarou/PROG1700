names = []
while True:
  print("Enter your name to be added to the list.")
  print("Enter 'quit' to exit.\n")
  first = input("What is your first name? ").strip().title()
  if first == 'Quit':
    break
  last = input("What is your last name? ").strip().title()
  name = f"{first} {last}"
  if name in names:
    print("That name is a duplicate.")
  else:
    names.append(name)
    for name in names:
      print(name)
