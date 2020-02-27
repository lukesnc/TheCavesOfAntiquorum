# File for enemy database and combat system

# includes
from TheCavesOfAntiquorum import items
from TheCavesOfAntiquorum.helpers import printSlow

from time import sleep
from random import random

# ENEMIES 

# Main enemy class (ALL ENEMIES SHARE THESE FUNCTIONS AND ATTRIBUTES)
class Enemy(object):
  # Consts
  UNKILLABLE = 999 # Health value given to an unkillable enemy

  # Variables that enemies have
  name = ""
  damage = None
  weapon = None
  health = None
  tauntMsg = ""
  allowedWeapons = []
  chanceToEncounter = 1/10

  # Returns a random weapon for newly spawned enemy to hold
  # Must pass in list of allowed weapons
  def getRandomWeapon(self):
    # Dictionary of enemy weapons
    enemyWeapons = {
      items.Stick: items.Stick(),
      items.Stone: items.Stone(),
      items.Club: items.Club(),
      items.Dagger: items.Dagger()
    }

    weaponReturned = False

    # Checks if the enemy is allowed to use the weapon, then rolls chance to recieve it
    while weaponReturned == False:
      for weapon in enemyWeapons:
        if ((weapon in self.allowedWeapons) and (random() < weapon.chanceToGet)):
          weaponReturned = True
          return enemyWeapons[weapon]

  # Combat functions
  def attack(self):
    try:
      print("the " + self.name + " swings its " + self.weapon.name)
    except:
      print("the " + self.name + " attacks")
    sleep(1)
    printSlow("the " + self.name + " deals " + str(self.damage) + " damage\n\n")
    return self.damage

  def takeDamage(self, damage):
    self.health = self.health - damage


# Sub-classes
    
class Rat(Enemy):
  name = "rat"
  damage = 2
  tauntMsg = "squeak"
  # For testing
  # chanceToEncounter = 1
  
  def __init__(self):
    super().__init__()
    self.health = 5

class Spider(Enemy):
  name = "spider"
  damage = 4
  tauntMsg = "bug noises"

  def __init__(self):
    super().__init__()
    self.health = 10

class UndeadSoldier(Enemy):
  name = "undead soldier"
  tauntMsg = "honor to those who stand before our god"
  allowedWeapons = [
    items.Stick,
    items.Stone,
    items.Club
  ]

  def __init__(self):
    super().__init__()
    self.health = 15
    self.weapon = self.getRandomWeapon()
    self.damage = self.weapon.damage
    
class Goblin(Enemy):
  name = "goblin"
  tauntMsg = "oh, the things that man desires"
  allowedWeapons = [
    items.Stick,
    items.Stone,
    items.Dagger
  ]

  def __init__(self):
    super().__init__()
    self.health = 8
    self.weapon = self.getRandomWeapon()
    self.damage = self.weapon.damage

class Spirit(Enemy):
  name = "spirit"
  damage = 1
  tauntMsg = "you don’t have the stone to finish paving your path"
  chanceToEncounter = 0.01

  def __init__(self):
    super().__init__()
    self.health = self.UNKILLABLE
