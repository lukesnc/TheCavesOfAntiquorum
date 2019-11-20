# Contains class player which holds inventroy and other useful values/functions

# includes
from TheCavesOfAntiquorum import const, items
from TheCavesOfAntiquorum.helpers import printSlow, clearScreen, shutDown, savePlayer

from time import sleep

class Player:
  # Consts
  MAX_HEALTH = 15
  ARMOR_MOD = 0.5

  def __init__(self):
    # Player variables (not regardless of instance)
    self.name = ""
    self.health = 15
    self.deaths = 0

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

  # Resets certain player values upon reload
  def reset(self):
    self.health = self.MAX_HEALTH


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
      self.health -= damage * self.ARMOR_MOD
    else:
      self.health -= damage

    # Check if player health is 0 or below and then die, otherwise nothing
    if self.health < 1:
      self.die()


  def die(self):
    # Incriments death variable
    self.deaths += 1

    clearScreen()
    print("your knees give out, and you fall to the floor")
    sleep(2)
    print("your vision fades, defeat setting in")
    sleep(2)
    print("blood is pouring from your wounds, there's no stopping this")
    sleep(2)
    print("you tip forward, your face smashing against the ground")
    sleep(2)
    printSlow("\nyou bleed out, and your heart stops\n")
    sleep(1)
    printSlow(".....")
    sleep(5)
    clearScreen()

    # Updates death count in save file
    save = open(const.SAVE_PATH, 'r')
    data = save.read()
    save.close()
    update = data.replace("DEATHS=" + str(self.deaths - 1), "DEATHS=" + str(self.deaths))
    save = open(const.SAVE_PATH, 'w')
    save.write(update)
    save.close()

    sleep(2)
    printSlow("\nSave file updated.\n")
    sleep(3)
    clearScreen()
    sleep(2)
    
    # Restart game at saved act
    savePlayer(self)
    shutDown()
    
