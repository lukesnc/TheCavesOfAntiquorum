# Items database
# Every items needs an item ID which will be stored in the users inventory if they have the item

# includes
from time import sleep

class UselessKey:
  ID = 1
  name = "bronze key"


class Dynamite:
  ID = 2
  name = "dynamite stick"


class JaggedRock:
  ID = 9
  name = "jagged rock"
  damage = 1

  def __init__(self):
    self.durability = 3

  def itemBreak(self):
    print("the jagged rock broke")
    return 0

  def attack(self, durability):
    if self.durability != 0:
      self.durability = self.durability - 1
      return 1
    else:
      self.itemBreak() 


class Fists:
  ID = 4
  name = "fists"

  def __init__(self):
    self.damage = 1
    self.durability = 10
    self.winded = False

  def swing(self):
    if self.winded == True:
      self.damage = .5


class BrokenWheel:
  ID = 3
  name = "broken wheel"
  damage = 1.5

  def __init__(self):
    self.durability = 3

  def swing(self):
    self.durability -= 1
    print("you swing the broken wheel")
    sleep(1)
    print("it deals 1 damage")



# ENEMY WIELDED ITEMS
# ITEM IDs BEGIN WITH 6


class Stick:
  ID = 61
  name = "stick"
  damage = 1

class Stone:
  ID = 62
  name = "stone"
  damage = 2

class Club:
  ID = 63
  name = "wooden club"
  damage = 3

