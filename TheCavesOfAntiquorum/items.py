# Items database
# Every items needs an item ID which will be stored in the users inventory if they have the item

class UselessKey:
  ID = 1
  name = "bronze key"

class Dynamite:
  ID = 2
  name = "dynamite stick"

class JaggedRock:
  ID = 2
  name = "jagged rock"

  def __init__(self):
    self.damage = 1
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
