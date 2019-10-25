# Colection of game-wide functions

# includes
from time import sleep
from TheCavesOfAntiquorum import const
import sys
from shutil import copyfile

# Displays when user doesn't put in what the game is looking for
def inputError(text):
  if text.lower() == "quit":
    shutDown()
  elif text == "pee pee poo poo":
    launchOriginalGame()
  else:
    printSlow("ERROR - Please use exact phrasing...\n\n")

def shutDown():
  print("Quitting game...")
  sleep(.5)
  sys.exit()

# Launches first ever draft of the game as an easter egg
def launchOriginalGame():
  sleep(1)
  clearScreen()
  print("Booting first draft of The Caves of Antiquorum...")
  sleep(3)
  clearScreen()
  sleep(2)
  from docs import original
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

# def writeItemToSave(itemID):
#   # Write item to save file
#   save = open(const.SAVE_PATH, 'a')
#   if itemID == 1:
#     save.write("=1\n")
#   else:
#     save.write("DYNAMITE=0\n")
#   save.close()