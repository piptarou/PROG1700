import random as r

new_character = "yes"

while new_character == "yes":
  name = input("What's your character's name? ")
  def health():
    health = r.randint(1, 7) * r.randint(1, 9)
    return health
  
  print(f"{name} has {health()}hp.")
  new_character = input("Want to roll some new health stats? ")