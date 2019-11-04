# Contains class player which holds inventroy and other useful values

from TheCavesOfAntiquorum import const, items

class Player:

  def __init__(self):
    # Player variables (not regardless of instance)
    self.name = ""
    self.health = 5

    # Inventory operates on a list of item IDs
    self.inventory = []
    self.getInventory()

    # Equipment
    self.weapon = 0
    self.armor = False 


  def getName(self):
    # User has no choice here
    input("Enter your name: ")
    print("your name is now joe")
    self.name = "joe"

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
