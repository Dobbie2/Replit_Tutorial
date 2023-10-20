import os
for i in range(1,1000):
  print(i)
  os.system("clear")

import os, time
print("Welcome")
print("to")
print("Replit")
time.sleep(2)

os.system("clear")

username = input("Username: ")

from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    input()

while True:
 os.system("clear")

  # Show the menu

  # take user's input

  # check whether you should call the play() subroutine depending on user's input