# Act 3

# KEY FEATURES
# inventory and equipment
# more lore of game explored
# combat and enemies

# includes
from TheCavesOfAntiquorum import player, items, const
from TheCavesOfAntiquorum.helpers import clearScreen, inputError, printSlow, printVerySlow

from time import sleep

# Globals
p1 = player.Player()
weapon = 0



def start():
  clearScreen()
  printSlow("======ACT=3======\n")
  sleep(1)
  printSlow("\n.....")
  input()
  clearScreen()
  sleep(3)
  