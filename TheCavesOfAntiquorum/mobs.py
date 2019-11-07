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

  r = randint(1, 10)
  if r < 3: # 1/3 to get stone
    w = items.Stone.ID
  elif r > 3 and r < 10: # 3/5 to get stick
    w = items.Stick.ID
  else: # 1/10 to get club
    w = items.Club.ID

  # w = randint(const.ENEMY_WEAPON_ID_MIN, const.ENEMY_WEAPON_ID_MAX)
  return enemyWeapon[w]

# Returns a random minor enemy
def getRandomEnemy():
  # Dictionary of enemies
  enemies = {
    Rat.name: Rat(),
    Spider.name: Spider(),
    UndeadSoldier.name: UndeadSoldier()
  }

  r = randint(1, 10)
  if r < 3: # 1/3 to get rat
    e = Rat.name
  elif r > 3 and r < 10: # 3/5 to get spider
    e = Spider.name
  else: # 1/10 to get undead soldier
    e = UndeadSoldier.name

  return enemies[e]
  
# Random enemy encounter, pass in class player
def encounterEnemy(player):
  e = getRandomEnemy()

# ENEMIES 

# Main enemy class (ALL ENEMIES SHARE THESE FUNCTIONS AND ATTRIBUTES)
class Enemy(object):
  # Variables that enemies have
  name = None
  damage = None
  weapon = None
  health = None

  # Combat functions
  def attack(self):
    return self.weapon.damage

  def takeDamage(self, damage):
    self.health = self.health - damage


# Sub-classes
    
class Rat(Enemy):
  name = "rat"
  damage = 2
  
  def __init__(self):
    self.health = 5

class Spider(Enemy):
  name = "spider"
  damage = 4

  def __init__(self):
    self.health = 10

class UndeadSoldier(Enemy):
  name = "undead soldier"

  def __init__(self):
    self.health = 15
    self.weapon = getRandomWeapon()
    self.damage = self.weapon.damage
    

