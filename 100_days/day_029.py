def PrettyText(color, word):
  if color == "purple":
    print("\033[0;35m", word, sep="", end="")
  elif color == "cyan":
    print("\033[0;36m", word, sep="", end="")
  elif color == "yellow":
    print("\033[1;33m", word, sep="", end="")
  elif color == "black":
    print("\033[0;30m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Color Subroutine")
print("I would like to argue that ", end="")
PrettyText("purple", "this")
PrettyText("reset", " is not technically purple, it's magenta. This is an important distinction for new color theory which now uses ")
PrettyText("cyan", "cyan ")
PrettyText("reset", ", ")
PrettyText("purple", "magenta ")
PrettyText("reset", ", ")
PrettyText("yellow", "yellow ")
PrettyText("reset", ", and ")
PrettyText("black", "black ")
PrettyText("reset", ". Also known as CMYK, and has been used in physical print for eons. RGB is terrible color theory for anything in a physical medium. \n")
print()
print("And yes, Oxford commas save lives.")