import os, time
email_list = []

def prettyPrint():
  os.system("cls")
  print("email_list")
  print()
  for index in range(len(email_list)):
    print(f"{index+1}: {email_list[index]}")
  time.sleep(1)

def get_spamming():
  for person in email_list:

    print(f"""Dear {person},
           It has come to our attention that you're missing out.
          On what? On the amazing Replit 100 days of code! 
          We insist you do it right away. 
          If you don't we will pass on your email address to every spammer we've ever encountered.
          We will also sign you up to the My Little Pony newsletter, because that's neat. 
          We might just do that anyway. 11
          
          Love and hugs, 
          Ian Spammington III""")
    time.sleep(1)

while True:
  print("1. Add email")
  print("2. Remove email")
  print("3. Show emails")
  print("4. Get SPAMMING?!")

  choice = input("Please select a number from the menu: ")
  if choice == "1":
    email = input("Email: ")
    email_list.append(email)
  elif choice == "2":
    prettyPrint() 
    email = input("Please type the email you wish to delete: ")
    if email in email_list:
      email_list.remove(email)
    prettyPrint() 
  elif choice == "3":
    prettyPrint() 
  elif choice == "4":
    get_spamming()
  time.sleep(1)
  os.system("cls")