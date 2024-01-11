while True:
  leap_year = input("Is it a leap year? Y/N ").lower()
  if leap_year == "n":
    seconds_in_year = 60*60*24*365
    print(f"the number in a normal year is {seconds_in_year}")
    break
  elif leap_year == "y":
    seconds_in_year = 60*60*24*366
    print(f"the number in a leap year is {seconds_in_year}")
    break
  else:
    print("Your input wasn't recognized")