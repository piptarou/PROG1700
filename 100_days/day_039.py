import random as r

word_list = ["aboleth", "tarrasque", "owlbear", "gnoll", "ettercap", "hobgoblin", "jackalwere", "manticore", "duergar", "demilich"]
guess = []
lives = 6

word = r.choice(word_list)

print("Monster Manual Hangman\n")

while True:

  letter = input("Guess a letter: ").lower()

  if letter in guess:
    print("You've already tried that!")
    continue

  guess.append(letter)
  
  if letter in word:
    print("One down!")
  else: 
    print("Try again!")
    lives -= 1
  
  all_letters = True
  print()
  for i in word:
    if i in guess:
      print(i, end = "")
    else:
      print("_", end = "")
      all_letters = False
  print()
  
  if all_letters:
    print(f"You won with {lives} lives left!")
    break
  
  if lives <= 0:
    print(f"You ran out of lives! The correct answer was {word}.")
    break
  else:
    print(f"Only {lives} lives left!")