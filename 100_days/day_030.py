print("30 Days of Replit So Far - Thoughts?")
print()
for i in range(1, 31):
  thought = input(f"Day {i}: ")
  print()
  text = f"You thought Day {i} was"
  print(f"{text: ^35}")
  print(f"{thought: ^35}\n")
