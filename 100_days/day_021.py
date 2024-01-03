print("===Let's practice our times tables!=== \n")
print("I'll give you 10 questions and you give me 10 answers!\n")
counter = 0

multiply = int(input("What number to multiply by? "))
for i in range (1,11):
  correct = i*multiply
  answer = int(input(f"{i} x {multiply} = "))
  if answer == correct:
    print("Nice!")
    counter +=1
  elif answer != correct:
    # I googled how to show 'not equal to'.
    print("Oops! The right answer is ", correct)
    
if counter == 10:
  print("Sweet! You got them all right!")
else:
  print("You only got", counter, "right.")
