def login():
  while True:
    username = input("What is your username? ")
    password = input("What is your password? ")
    if username == "volothamp" and password == "monsterzrule":
      print("Welcome back!")
      break
    else:
      print("Wrong username or password!")

print("The Yawning Portal Login")
login()


#You  can also use:
# if username == "" and password == "":
#   return True