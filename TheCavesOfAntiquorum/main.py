# The Caves of Antiquorum
# Author: Luke Simone

# Main file / act 1

# includes
from time import sleep
import datetime

from TheCavesOfAntiquorum.helpers import clearScreen, inputError, startAct
from TheCavesOfAntiquorum import const, items

# Act 1 globals
uselessKey = 0 # First key found on the ground
startRoom = 0 # Allows revist of room for more clues

def furtherInTheHole():
  writeKeyToSave()

  print("you step further down into the depths of the cave\n")
  sleep(5)
  print("the ground begins to shake")
  sleep(1)
  print("the walls around you tremble")
  sleep(1)
  print("dust begins to fall from the cieling\n")
  sleep(5)
  print("the rocks have fallen and closed the path behind you")
  sleep(5)
  input("there is only one way to go: forward...")
  startAct(2)

def writeKeyToSave():
  # Write key to save
  save = open(const.SAVE_PATH, 'a')
  if uselessKey == 1:
    save.write("USELESSKEY=1\n")
  else:
    save.write("USELESSKEY=0\n")
  save.close()

  print("\nSave file updated.\n")
  sleep(1)

def inspectDoor():
  sleep(1)
  print("you jiggle the knob")
  print("it requires a key\n")

  if uselessKey == 0:
    sleep(2)
    paths()
  elif uselessKey == 1:
    sleep(1)
    print("the key you have does not fit\n")
    paths()
 
def throughHole():
  global uselessKey
  sleep(1)
  print("the air gets noticeably colder, the howl ceases\n")
  sleep(1)
  print("it's very dark, you find yourself stumbling, however you can see a faint glow further on\n")
  sleep(1)
  print("keep going?\n")
  
  while True:
    print("keep going or go back")
    option = input("> ")

    if option == "keep going" and uselessKey == 0:
      sleep(1)
      print("you come to a bend in the tunneling, a key is stuck in the ground")
      sleep(1)
      print("pick it up?\n")
      
      while True:
        print("pick it up or keep going")
        option2 = input("> ")

        if option2 == "pick it up" or option2 == "pick up":
          uselessKey = 1
          print("picked up: " + items.UselessKey.name + "\n")
          sleep(1)

          while True:
            print("keep going or go back")
            option3 = input("> ")

            if option3 == "keep going":
              furtherInTheHole()
              break
            elif option3 == "back" or option3 == "go back":
              paths()
              break
            inputError(option3)
          break
        elif option2 == "keep going":
          furtherInTheHole()
          break
        inputError(option2)
      break
    elif option == "keep going" and uselessKey == 1:
      furtherInTheHole()
      break
    elif option == "go back" or option == "back":
      paths()
      break
    inputError(option)

def paths():
  print("the path in front of you seeps cold air, and appears as a dark hole in the wall, there is a faint howl\n")
  sleep(2)
  print("maybe wind, maybe beast\n")
  sleep(2)
  print("the path behind is shut by a door\n")
  
  while True:
    print("inspect door, through hole, back")
    option = input("> ")

    if option == "inspect door" or option == "door":
      inspectDoor()
      break
    elif option == "through hole" or option == "hole":
      throughHole()
      break
    elif option == "back":
      roomsOrPaths()
      break
    inputError(option)
 
def roomsOrPaths():
  global startRoom
  print("describe paths or room?\n")
  
  while True:
    print("paths or room")
    option = input("> ")

    if option == "room" and startRoom == 0:
      print("the room is barren")
      print("the ceiling depicts some artistic endeavor\n")
      sleep(3)
      print("you can barely make out the hieroglyphics\n")
      sleep(2)
      print("are those... teeth?\n")
      startRoom = 1
      roomsOrPaths()
      break
    elif option == "room" and startRoom == 1:
      sleep(1)
      print("you take another glance at the painting")
      sleep(2)
      print("you see a man bleeding\n")
      roomsOrPaths()
      break
    elif option == "paths":
      paths()
      break
    inputError(option)
  
def lightIt():
  print("you get up and look around")
  print("you're standing in the center of a stone room\n")
  sleep(3)
  print("there are two openings in the room, one behind you and one in front\n")
  roomsOrPaths()
 
# Story begins
def beginStory():
  print("you wake up, your head hurts\n")
  sleep(1)
  print("it's dark all around, but there is a small unlit lantern next to you, light it?\n")
  sleep(1)

  while True:
    print("leave it or light it")
    sleep(1)
    option = input("> ")
    
    if option == "leave it":
      start()
      break
    elif option == "light it":
      print("you're embraced by a comforting warmth\n")
      sleep(2)
      lightIt()
      break
    inputError(option)

def start():
  clearScreen()
  print("Welcome to The Caves of Antiquorum\nby Joseph Alberici and Luke Simone\n")
  print("Type \"quit\" and press ENTER to exit the game at any time.")
  input("Press ENTER to begin the game...")
  clearScreen()
  sleep(2)
  beginStory()

# Creates a save file (or overwrites an existing one) 
# Writes the time of creation and that the user is in act 1
def createSave():
  print("Creating save file...")

  save = open(const.SAVE_PATH, "w+")
  save.write("SAVE FILE FOR THE CAVES OF ANTIQUORUM\n")
  save.write("CREATED " + str(datetime.datetime.now()) + "\n\n")
  save.write("ACT=1\n")
  save.write("DEATHS=0\n")
  save.write("\n=======ITEMS=======\n\n")
  save.close()

  sleep(5)
  print("Done")
  sleep(.5)

# First function that's called, begins the program
def boot():
  # Checks if previous save exists, if not creates one
  saveMade = False # variable prevents double creation
  try: 
    save = open(const.SAVE_PATH, 'r')
  except OSError:
    createSave()
    saveMade = True

  # Jump to the different acts based on save
  save = open(const.SAVE_PATH, 'r')

  # Don't use .read() in multiple conditions make a var instead and check that
  saveData = save.read()
  if "ACT=2" in saveData:
    save.close()
    startAct(2)
  elif "ACT=3" in saveData:
    save.close()
    startAct(3)
  else: # Something in the save file is corrupt or haven't left act 1
    save.close()
    if saveMade == False:
      createSave()
    start()

boot()
