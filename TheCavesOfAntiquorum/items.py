# Items database
# Every items needs an item ID which will be stored in the users inventory if they have the item

# includes
from random import randint

# GENERAL ITEMS

class UselessKey:
  ID = 1
  name = "bronze key"


class Dynamite:
  ID = 2
  name = "dynamite stick"

# PLAYER WEAPONS
# Player weapons CAN break

class Fists:
  ID = 4
  name = "fists"
  swingMsg = "you swing your fists"

  def __init__(self):
    self.damage = 1
    self.durability = 10
    self.winded = False

  def swing(self):
    if self.winded == True:
      self.damage = .5


class RustyDagger:
  ID = 5
  name = "rusty dagger"
  damage = 3
  swingMsg = "you evsicerate the enemy with your rusty dagger"

  def __init__(self):
    self.durability = 5


class BreakingWheel:
  ID = 3
  name = "the breaking wheel"
  damage = 4
  swingMsg = "you crush their ribs with the breaking wheel"

  def __init__(self):
    self.durability = 3


# ENEMY WIELDED ITEMS
# ITEM IDs BEGIN WITH 6
# Enemy items DON'T break

# class EnemyItem:
#   ID = item ID
#   name = weapon name
#   damage = damage weapon deals
#   chanceToGet = chance enemy will spawn with item

class Stick:
  ID = 61
  name = "stick"
  damage = 4
  chanceToGet = 3/5
  
  def __init__(self):
    self.durability = randint(1, 3)

class Stone:
  ID = 62
  name = "stone"
  damage = 2
  chanceToGet = 1/3

  def __init__(self):
    self.durability = randint(1, 4)

class Club:
  ID = 63
  name = "wooden club"
  damage = 7
  chanceToGet = 1/10

  def __init__(self):
    self.durability = randint(1, 2)

class Dagger:
  ID = 64
  name = "dagger"
  damage = 5
  chanceToGet = 1/5

  def __init__(self):
    self.durability = randint(2, 3)
