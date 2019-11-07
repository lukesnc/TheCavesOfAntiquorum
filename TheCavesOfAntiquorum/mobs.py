# NPC database

from TheCavesOfAntiquorum import items, const
from random import randint

from time import sleep

# Returns a random weapon for newly spawned enemy to hold
def getRandomWeapon(rMin, rMax):
  # Dictionary of enemy weapons
  enemyWeapon = {
    items.Stick.ID: items.Stick(),
    items.Stone.ID: items.Stone(),
    items.Club.ID: items.Club()
  }

  r = randint(rMin, rMax)
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
  # Enemy and player
  e = getRandomEnemy()
  p = player

  playerActions = ["attack", "cower", "run"]
  enemyActions = ["attack", "taunt"]

  combatFinished = False

  # While the enemy and player are alive
  while combatFinished == False:
    # Check if anyone is dead
    if e.health < 0:
      combatFinished = True
    elif p.health < 0:
      p.die()



# ENEMIES 

# Main enemy class (ALL ENEMIES SHARE THESE FUNCTIONS AND ATTRIBUTES)
class Enemy(object):
  # Variables that enemies have
  name = None
  damage = None
  weapon = None
  health = None
  tauntMsg = None

  # Combat functions
  def attack(self):
    return self.weapon.damage

  def takeDamage(self, damage):
    self.health = self.health - damage

  def taunt(self):
    print(self.tauntMsg)
    sleep(1)


# Sub-classes
    
class Rat(Enemy):
  name = "rat"
  damage = 2
  tauntMsg = "squeak"
  
  def __init__(self):
    super().__init__()
    self.health = 5

class Spider(Enemy):
  name = "spider"
  damage = 4
  tauntMsg = "bug noises"

  def __init__(self):
    super.__init__()
    self.health = 10

class UndeadSoldier(Enemy):
  name = "undead soldier"
  tauntMsg = "honor to those who stand before our god"

  def __init__(self):
    super.__init__()
    self.health = 15
    self.weapon = getRandomWeapon(0, 10)
    self.damage = self.weapon.damage
    