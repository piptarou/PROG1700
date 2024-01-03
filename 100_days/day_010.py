my_bill = float(input("What was the bill? "))
number_of_people = int(input("How many people? "))
amount_of_tip = int(input("What is the tip percentage you'd like to leave? "))
tip = 1 + (amount_of_tip/100)
if amount_of_tip < 10:
  print("You should tip more")
answer = round(my_bill / number_of_people*tip, 2)
print(f"You all owe me {answer}")

