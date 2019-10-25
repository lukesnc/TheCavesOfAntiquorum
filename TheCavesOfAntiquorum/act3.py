# Act 3

# KEY FEATURES
# inventory
# more lore of game explored
# weapon found at the end

# includes
from time import sleep

from TheCavesOfAntiquorum import player, items, const
from TheCavesOfAntiquorum.helpers import clearScreen, inputError, printSlow, printVerySlow

# Globals
p1 = player.Player()
weapon = 0

def start():
  clearScreen()
  printSlow("=========================\n")
  printSlow("==========ACT=3==========\n")
  printSlow("=========================\n")
  sleep(1)
  printSlow("\nENTER to continue...\n")
  input()
  clearScreen()
  sleep(3)
  