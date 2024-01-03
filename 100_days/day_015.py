fun = "yes"

while fun == "yes":
  sound = input("Do you want to hear a cat, cow, or dog?\n" )
  if sound == "cow":
    print("Moo!\n")
  elif sound == "cat":
    print("Meow!\n")
  elif sound == "dog":  
    print("Woof!\n")
  fun = input("Are you having fun?: \n")