# Act 3

# KEY FEATURES
# weapons and equipment
# more lore of game explored
# combat and enemies

# includes
from TheCavesOfAntiquorum import items, const
from TheCavesOfAntiquorum.helpers import clearScreen, inputError, printSlow, printVerySlow, loadPlayer
from TheCavesOfAntiquorum.player import Player
from TheCavesOfAntiquorum.combat import CombatSystem

from time import sleep

# Globals
rubbleBlownUp = False

try:
  p1 = loadPlayer()
except:
  p1 = Player()
c = CombatSystem()


# Room after rubble is blown, containing lore of game and shitty dagger
def loreRoom():
  print("you emerge into a very odd room\n")
  sleep(1)
  print("the room is small, with many paths leading to other rooms")
  sleep(2)
  print("there are slimy, tentacle-like apendages rising from the ground")
  sleep(2)
  print("straight ahead is a word engraved on the wall: ", end='')
  sleep(1.5)
  printVerySlow("Arenam")
  sleep(3)
  print("\nin the middle of the room sits a podium\n")
  sleep(1)
  while True:
    print("investiage podium or go back")
    option = input("> ")

    if option == "investigate":
      print("you step up to the podium")
      sleep(1)
      print("on it lies a rusty dagger")
      sleep(1)
      while True:
        print("\ntake the dagger?\n\nyes or no")
        option2 = input("> ")

        if option2 == "yes":
          sleep(1)
          print("you pick up the dagger")
          sleep(1)
          print("you spin it around, admiring its rust", end='')
          sleep(2)
          print(", its fragility", end='')
          sleep(1.5)
          print(", and its shittiness")
          sleep(2)
          printSlow("equipped: " + items.RustyDagger.name + "\n\n")
          p1.weapon = items.RustyDagger()
          sleep(1)
          break
        elif option2 == "no":
          sleep(1)
          print("upon further consideration...")
          sleep(3)
          print("weapons are overrated")
          sleep(2)
          print("punching everything to death is way more fun anyway\n")
          sleep(2)
          break
        inputError(option2)
      # Continuing whether player has dagger or not
      print("you continue on through the room")
      sleep(1)
      print("your " + p1.weapon.name + " at the ready")
      sleep(2)
      print("\nin your excitement you failed to notice a book at your feet")
      sleep(1)
      # continue here

      break
    elif option == "go back" or option == "back":
      attemptRock()
      break
    inputError(option)
    

# Story of act 3 starts here
def attemptRock():
  global rubbleBlownUp
  if not rubbleBlownUp:
    print("it's darker than before, but the rubble is still there")
    sleep(1)
    print("and an explosive in your hands")
    sleep(2)
    print("\nyou need something to light the dynamite with")
    sleep(2)
  else:
    print("it's darker than before, and your ears are ringing a bit")
    sleep(1)

  while True:
    print("\nlook around?\n\nyes or no")
    option = input("> ")

    if option == "yes" and not rubbleBlownUp:
      print("you look around on the ground, pushing over rocks and feeling around on the walls")
      sleep(1)
      print("you find a piece of flint\n")
      sleep(1)
      print("you grab another rock and spark the flint over the fuse", end='')
      sleep(1)
      printVerySlow(".......")
      printSlow("\nboom!")
      rubbleBlownUp = True
      p1.inventory.remove(items.Dynamite.ID)
      sleep(2)
      print("\nthe rock was blown away, leaving a path forward")
      sleep(1)
      while True:
        print("\nkeep going or go back")
        option2 = input("> ")
        
        if option2 == "keep going":
          loreRoom()
          break
        elif option2 == "go back" or option2 == "back":
          attemptRock()
          break
        inputError(option2)
      break
    elif option == "yes" and rubbleBlownUp:
      print("the rubble is already blown up, idiot")
      sleep(2)
      print("\nyou step forward into the room")
      sleep(1)
      loreRoom()
    elif option == "no":
      print("you decide against looking around the room")
      sleep(2)
      print("\nwhy not give youself a name?")
      sleep(1)
      p1.getName()
      sleep(2)
      clearScreen()
      attemptRock()
      break
    inputError(option)

def start():
  clearScreen()
  printSlow("======ACT=3======\n")
  sleep(1)
  printSlow("\n.....")
  input()
  clearScreen()
  sleep(3)
  attemptRock()

  # combat testing
  # c.testEnemyEncounter(p1, 1)
