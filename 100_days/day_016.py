print("Welcome to Guess the Nightmare Before Christmas Lyric!\n")
print("Figure out the missing word as quickly as you can!\n")


counter = 0
while True:
  lyrics = input("You're jokin', you're jokin', I can't believe my ________: ")
  if lyrics == "eyes" or lyrics == "Eyes":
    print("Nice!")
    counter +=1
  else:
    print("Try again!")
  if lyrics == "eyes":
    break  
print("I bet you watch this movie twice a year! ")
print("You got the right word in", counter, "attempt(s).")