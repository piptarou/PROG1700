#Character Fight Sim
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

def damage_gen():
     damage = r.randint(1, 7)
     return damage

print("### BATTLE SIM ###")

p1_name = name_gen()
p1_race = race_gen()
p1_str = strength_gen()
p1_hp = health_gen()

print(f"{p1_name} the {p1_race}'s stats:")
print(f"HP: {p1_hp}")
print(f"STR: {p1_str} \n")

print("Who is the challenger? \n")
    
p2_name = name_gen()
p2_race = race_gen()
p2_str = strength_gen()
p2_hp = health_gen()

print(f"{p2_name} the {p2_race}'s stats:")
print(f"HP: {p2_hp}")
print(f"STR: {p2_str} \n")

round = 1
winner = None

while True:
    time.sleep(1)
    os.system("cls")
    print("## FIGHT ## \n")

    p1_dmg = damage_gen()
    p2_dmg = damage_gen()

    difference = abs(p1_str - p2_str) + 1

    if p1_dmg > p2_dmg:
        p2_hp -= difference
        if round == 1:
            print(f"{p1_name}'s weapon makes purchase! \n")
        else:
            print(f"{p1_name} wins round {round}\n")
    elif p2_dmg > p1_dmg:
        p1_hp -= difference
        if round == 1:
            print(f"{p2_name}'s weapon makes purchase! \n")
        else:
            print(f"{p2_name} wins round {round}!\n")
    elif p1_dmg == p2_dmg:
        print(f"You both blocked effectively! Round {round} is a draw! \n")
    
    # print(f"{p1_dmg}-----{p2_dmg} \n") 
    #The above line of code was used to show if the rolls were randomized

    print(f"{p1_name}'s HP: {p1_hp} \n")
    print(f"{p2_name}'s HP: {p2_hp} \n")        

    if p1_hp <=0 :
        print(f"{p1_name} has died!")
        winner = p2_name
        break
    elif p2_hp <=0 :
        print(f"{p2_name} has died!")
        winner = p1_name
        break
    else:
        print("Next round! \n")
        round += 1

time.sleep(1)
os.system("cls")
print("## BATTLE SIM ## \n")
print(f"{winner} has won in {round} rounds!")
