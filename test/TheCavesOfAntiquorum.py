# Run this file to begin the game

import sys


class Game:
  def start(self):
    # Jumps to main.py
    from TheCavesOfAntiquorum import main


if __name__ == "__main__":
  g = Game()
  g.start()
  sys.exit()
  