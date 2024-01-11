#I wanted to make sure that all variables were defined at the top and then wanted to make it impossible to use '0' as an increment.

print("Let's list some numbers!\n")

start = int(input("Starting number: "))
end = int(input("Ending number: "))
incr = int(input("In what increment?: "))
while True:
  if (start > end) and incr >=0:
    print("You gotta choose a bigger ending number! ")
    end = int(input("Ending number: "))
    incr = int(input("In what increment?: "))
    if (start < end) and incr <=0:
      print("Use at least '1' for an increment!")
      incr = int(input("In what increment?: "))
      for i in range (start, end, incr):
        print(i)
    for i in range (start, end, incr):
      print(i)
  elif (start < end) and incr <=0:
    print("Use at least '1' for an increment!")
    incr = int(input("In what increment?: "))
    for i in range (start, end, incr):
      print(i)
  else:
    for i in range (start, end, incr):
      print(i)
