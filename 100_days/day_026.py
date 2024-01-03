from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False 
  while True:
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : "))
    if stop_playback == 2:
      source.paused = True 
      return
    else: 
      continue

while True:
  os.system("clear") 
  
  print("Music Player")
  print("Press 1 to play: ")
  time.sleep(1)
  print("Press 2 to exit: ")
  time.sleep(1)

  choice = input("Press anything else to see the menu again: ").lower()

  if choice == "1":
    play()
  elif choice == "2":
    exit()
  else:
    continue