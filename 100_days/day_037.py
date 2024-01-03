print("🌟Star Wars Name Generator🌟\n")

first = input("Input your first name: ")
last =input("Input your last name: ")
maiden = input("Input your mother's maiden name: ")
city = input("Input the city where you were born: ")

starname = f"{first[:3]}{last[:3]} {maiden[:2]}{city[-3:]}".title()
print(f"Your Star Wars name is {starname}")
