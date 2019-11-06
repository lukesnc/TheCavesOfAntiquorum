# NPC database

from TheCavesOfAntiquorum import items, const
from random import randint

# Returns a random weapon for newly spawned enemy to hold
def getRandomWeapon():
  # Dictionary of enemy weapons
  enemyWeapon = {
    items.Stick.ID: items.Stick(),
    items.Stone.ID: items.Stone(),
    items.Club.ID: items.Club()
  }

  w = randint(const.ENEMY_WEAPON_ID_MIN, const.ENEMY_WEAPON_ID_MAX)
  return enemyWeapon[w]

# ENEMIES 
    
class Rat:
  name = "rat"
  
  def __init__(self):
    self.health = 5

class Spider:
  name = "spider"

  def __init__(self):
    self.health = 10

class UndeadSoldier:
  name = "undead soldier"

  def __init__(self):
    self.health = 15
    self.weapon = getRandomWeapon()
    
  def attack(self):
    return self.weapon.damage

  def takeDamage(self, damage):
    self.health = self.health - damage

