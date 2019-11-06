# Act 3

# KEY FEATURES
# weapons and equipment
# more lore of game explored
# combat and enemies

# includes
from TheCavesOfAntiquorum import player, items, const
from TheCavesOfAntiquorum.helpers import clearScreen, inputError, printSlow, printVerySlow

from time import sleep

# Globals
p1 = player.Player()

# Story of act 3 starts here
def attemptRock():
  print("it's darker than before, but the rubble is still there")
  sleep(1)
  print("and an explosive in your hands")
  sleep(2)
  print("\nyou need something to light the dynamite with")
  sleep(2)

  while True:
    print("\nlook around?\n\nyes or no")
    option = input("> ")

    if option == "yes":
      print("you look around on the ground, pushing over rocks and feeling around on the walls")
      sleep(1)
      print("you find a piece of flint")
      # FINISH THIS
      break
    elif option == "no":
      print("you decide against looking for something to light the dynamite with")
      sleep(2)
      printSlow("\nwhy not give youself a name?\n")
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
  