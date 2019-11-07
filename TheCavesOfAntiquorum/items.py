# Items database
# Every items needs an item ID which will be stored in the users inventory if they have the item

# includes


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

  def __init__(self):
    self.damage = 1
    self.durability = 10
    self.winded = False

  def swing(self):
    if self.winded == True:
      self.damage = .5


class Dagger:
  ID = 5
  name = "rusty dagger"
  damage = 4

  def __init__(self):
    self.durability = 3


class BreakingWheel:
  ID = 3
  name = "the breaking wheel"
  damage = 4

  def __init__(self):
    self.durability = 3


# ENEMY WIELDED ITEMS
# ITEM IDs BEGIN WITH 6
# Enemy items DON'T break

class Stick:
  ID = 61
  name = "stick"
  damage = 4

class Stone:
  ID = 62
  name = "stone"
  damage = 2

class Club:
  ID = 63
  name = "wooden club"
  damage = 7

