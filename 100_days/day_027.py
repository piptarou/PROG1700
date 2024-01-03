#I based this day's challenge on stats used in D&D 5e.

import random as r
import os, time

def name_gen():
    name = input("What's your character's name? ").capitalize()
    return name

def race_gen():
    race = input("Are they a halfling, elf, human, half-orc, or dwarf? \n").lower()
    return race

def health_gen():
        health = r.randint(1, 7) * r.randint(1, 13)
        return health

def strength_gen():
    strength = r.randint(1, 7) * r.randint(1, 5)
    return strength

def intelligence_gen():
    intelligence = r.randint(1, 7) * r.randint(1, 5)
    return intelligence

def charisma_gen():
    charisma = r.randint(1, 7) * r.randint(1, 5)
    return charisma

def wisdom_gen():
    wisdom = r.randint(1, 7) * r.randint(1, 5)
    return wisdom

def dexterity_gen():
    dexterity = r.randint(1, 7) * r.randint(1, 5)
    return dexterity

def constitution_gen():
    constitution = r.randint(1, 7) * r.randint(1, 5)
    return constitution

SLOGANS = ['Adventure hinges on more than just a throw of the dice.', 
           'Be careful of where you decide to turn into a goldfish.',
           'The game has just begun.',
           'The worst rolls tell the best stories.',
           'Tip: Some Dungeon Masters can be bribed with snacks.']

def slogan_gen():
    slogan_number = r.randint(0,4)
    return SLOGANS[slogan_number]

new_character = "yes"

print("So you wanna make a hero, but don't have dice. Well, luckily you have this handy dandy character creator.")

while new_character == "yes":
    os.system("cls")
    name = name_gen()
    race = race_gen()
    strength = strength_gen()
    intelligence = intelligence_gen()
    charisma = charisma_gen()
    wisdom = wisdom_gen()
    dexterity = dexterity_gen()
    constitution = constitution_gen()
    os.system("cls") 
    
    print(f"{name} the {race}'s stats:")
    print(f"HP {health_gen()}")
    print(f"STR {strength_gen()}")
    print(f"INT {intelligence_gen()}")
    print(f"CHA {charisma_gen()}")
    print(f"WIS {wisdom_gen()}")
    print(f"DEX {dexterity_gen()}")
    print(f"CON {constitution_gen()}\n")

    time.sleep(1)
    print(f"{slogan_gen()} \n")

    time.sleep(1)

    again = input("Want to roll a new character? \n")
    
    if again == "no" or again == "No":
      exit()