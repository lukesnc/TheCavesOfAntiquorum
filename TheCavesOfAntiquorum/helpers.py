# Colection of game-wide functions

# includes
from TheCavesOfAntiquorum import const

from time import sleep
import sys
from shutil import copyfile
import pickle
from random import random

# Displays when user doesn't put in what the game is looking for
def inputError(text):
  if text.lower() == "quit":
    shutDown()
  else:
    printSlow("ERROR - Please use exact phrasing...\n\n")

# Quits the game
def shutDown():
  print("Quitting game...")
  sleep(.5)
  sys.exit()

# Letters print accross line rapidly instead of all appearing at once
def printSlow(str):
  for letter in str:
    print(letter, end='')
    sleep(.03)

# Same as above just very slow
def printVerySlow(str):
  for letter in str:
    print(letter, end='')
    sleep(.4)

# Quick function to clear text off screen
def clearScreen():
  print("\n" * 50)

# Updates the save file to checkpoint the player at an act and begins from first function of next act
def startAct(act):
  # Creates backup of save before updating 
  copyfile(const.SAVE_PATH, const.SAVE_BACKUP_PATH)

  # Updates act in save file
  save = open(const.SAVE_PATH, 'r')
  data = save.read()
  save.close()
  update = data.replace("ACT=" + str(act - 1), "ACT=" + str(act))
  save = open(const.SAVE_PATH, 'w')
  save.write(update)
  save.close()

  # Continues game
  print("\nSave file updated.")
  sleep(1)
  if act == 2:
    from TheCavesOfAntiquorum import act2
    act2.start()
  elif act == 3:
    from TheCavesOfAntiquorum import act3
    act3.start()
  #else:
    # last act or end game

# Pass in object of class Player to save to a file
def savePlayer(obj):
  with open(const.PLAYER_OBJ_PATH, 'wb') as output:
    pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
  output.close()

# Reloads object of player from file with a RETURN so
# set object in story equal to this function
def loadPlayer():
  with open(const.PLAYER_OBJ_PATH, 'rb') as infile:
    loadedObj = pickle.load(infile)
  infile.close()
  return loadedObj
