# You can also do dictionary = {"name": input("What's your name? "), "bday": input("Bday? ")} etc.

name = input("Input your name: ")
bday = input("Input your bday: ")
email = input("email? ")
address = input("address? ")
phone = input("phone number? ")
  
dictionary = {"name":name, "bday":bday, "email":email,
              "address":address, "phone":phone
             }
print(f"Hi {dictionary['name']}, Our dictionary says you were born on {dictionary['bday']}, we can reach you at {dictionary['phone']}, {dictionary['email']}, or write to {dictionary['address']}.")