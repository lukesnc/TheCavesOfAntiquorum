# NPC database

from TheCavesOfAntiquorum import items, const
from random import randint, random

from time import sleep

# Returns a random weapon for newly spawned enemy to hold
# Must pass in list of allowed weapons
def getRandomWeapon(allowed):
  # Dictionary of enemy weapons
  enemyWeapon = {
    items.Stick: items.Stick(),
    items.Stone: items.Stone(),
    items.Club: items.Club(),
    items.Dagger: items.Dagger()
  }

  weaponReturned = False

  # i is for every weapon in the dictionary
  # Checks if the enemy is allowed to use the weapon, then rolls chance to recieve it
  while weaponReturned == False:
    for i in enemyWeapon:
      if (enemyWeapon[i] in allowed[i]) and (random() < enemyWeapon[i].chanceToGet):
        weaponReturned = True
        return enemyWeapon[i]


# Returns a random minor enemy
def getRandomEnemy():
  # Dictionary of enemies
  enemies = {
    Rat: Rat(),
    Spider: Spider(),
    UndeadSoldier: UndeadSoldier()
  }

  enemyReturned = False

  # Rolls chance to encounter wild enemies
  while enemyReturned == False:
    for i in enemies:
      if (random() < enemies[i].chanceToEncounter):
        enemyReturned = True
        return enemies[i]


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
  name = ""
  damage = None
  weapon = None
  health = None
  tauntMsg = ""
  allowedWeapons = []
  chanceToEncounter = 1/5

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
    super().__init__()
    self.health = 10

class UndeadSoldier(Enemy):
  name = "undead soldier"
  tauntMsg = "honor to those who stand before our god"
  allowedWeapons = [
    items.Stick.ID,
    items.Stone.ID,
    items.Club.ID
  ]

  def __init__(self):
    super().__init__()
    self.health = 15
    self.weapon = getRandomWeapon(self.allowedWeapons)
    self.damage = self.weapon.damage
    
class Goblin(Enemy):
  name = "goblin"
  tauntMsg = "oh, the things that man desires"
  allowedWeapons = [
    items.Stick.ID,
    items.Stone.ID,
    items.Dagger.ID
  ]

  def __init__(self):
    super().__init__()
    self.health = 8
    self.weapon = getRandomWeapon(self.allowedWeapons)
    self.damage = self.weapon.damage

class Spirit(Enemy):
  name = "spirit"
  damage = 1
  tauntMsg = "you don’t have the stone to finish paving your path"
  chanceToEncounter = 0.02

  def __init__(self):
    super().__init__()
    self.health = const.UNKILLABLE