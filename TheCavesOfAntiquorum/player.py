# Contains class player which holds inventroy and other useful values

from TheCavesOfAntiquorum import const, items

class Player:

  def __init__(self):
    # Player variables (not regardless of instance)
    self.name = ""
    self.health = 3
    self.armor = False 

    # Inventory operates on a list of item IDs
    self.inventory = []

    self.getInventory()

  def getName(self):
    # User inputs name
    n = input("Enter your name: ")
    self.name = n

  # Loads the users inventory based on save file
  def getInventory(self):
    self.checkUselessKey()
    self.checkDynamite()

  # Determines if they have the key
  def checkUselessKey(self):
    save = open(const.SAVE_PATH, 'r')
    if "USELESSKEY=1" in save.read():
      self.inventory.append(items.UselessKey.ID)
    save.close()

  # Determines if they have the explosive
  def checkDynamite(self):
    save = open(const.SAVE_PATH, 'r')
    if "DYNAMITE=1" in save.read():
      self.inventory.append(items.Dynamite.ID)
    save.close()
