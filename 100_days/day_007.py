animal = input("Are you a cat person or a dog person? ")
if animal == "cat":
  crep = input("Oh yeah? Did you know that they are crepuscular? ")
  if crep == "yes":
    print("Oh, you think you're pretty smart, eh? ")
  elif crep == "no":
    print("Oh, I see you've never been awoken by a cat at 5am." )
  anth = input("Did you know that more anthrozoology studies have been about dogs? ")
  if anth == "yes":
    fair = input("Do you think that's fair? ")
    if fair == "no":
      print("Alright, you're one cool cat. Now get off the internet and let your owner finish working on the light box you're using. ")
    if fair == "yes":
      print("You're probably a dog, go eat some shoes. Or something.")
  elif anth == "no":
    nofair = input("Well they have. Do you think that's fair? ")
    if nofair == "no":
      print("Alright, you're one cool cat. Now get off the internet and let your owner finish working on the light box you're using. ")
      if nofair == "yes":
        print("You're probably a dog, go eat some shoes. Or something.")
if animal == "dog":
  dach = input("Oh yeah? Did you know that dachshunds were originally bred to fight badgers? ")
  if dach == "no":
    print("Well nobody would ever expect that from a weiner dog, so I'll let that slide. ")
  elif dach == "yes":
    print("Well lookit you smartypants. Knows so much about dogs.")
  anthro = input("Did you know that more anthrozoology studies have been about dogs instead of cats? ")
  if anthro == "yes":
    yesfair = input("Do you think that's fair? ")
    if yesfair == "no":
      print("Alright, you're one cool cat. Now get off the internet and go soak up some sun. ")
    elif yesfair == "yes":
      print("Go eat some shoes.")
  elif anthro == "no":
    nope = input("Well they have. Do you think that's fair? ")
    if nope == "no":
      print("Alright, you're one cool cat. Now get off the internet and go lay in the sun. ")
    if nope == "yes":
      print("You're probably a dog, go eat some shoes.")