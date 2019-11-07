# Contains class player which holds inventroy and other useful values

# includes
from TheCavesOfAntiquorum import const, items

class Player:

  def __init__(self):
    # Player variables (not regardless of instance)
    self.name = ""
    self.health = 15
    self.MAX_HEALTH = 15

    # Inventory operates on a list of item IDs
    self.inventory = []
    self.getInventory()

    # Equipment
    self.weapon = items.Fists()
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


  # COMBAT

  # Tests if there is a weapon, if its broken, and then returns damage 
  # vaue to be used on the enemy's takeDamage() function
  def attack(self):
    try:
      if weapon.durability > 0:
        weapon.durability -= 1
        return self.weapon.damage
      else:
        print("your " + self.weapon.name + " broke")
    except:
      print("you have no weapon")

  # Take damage from enemy in as parameter and subtract from player health
  def takeDamage(self, damage):
    # Checks if player has armor and takes damage accordingly
    if self.armor == True:
      self.health -= damage * const.ARMOR_MOD
    else:
      self.health -= damage

    # Check if player health is 0 or below and then die, otherwise nothing
    if self.health < 1:
      self.die()

  # Player eats enemies to regain health
  def eat(self):
    print("temp")
    # FINISH THIS

  def die(self):
    print("die")
    # FINISH THIS

  def dieForReal(self):
    print("die fr")
    # FINISH THIS
  