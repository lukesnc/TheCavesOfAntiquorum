# File for enemy database and combat system

from TheCavesOfAntiquorum import items, const
from TheCavesOfAntiquorum.helpers import clearScreen, printSlow, inputError

from random import randint, random
from time import sleep

# Returns a random weapon for newly spawned enemy to hold
# Must pass in list of allowed weapons
def getRandomWeapon(allowed):
  # Dictionary of enemy weapons
  enemyWeapons = {
    items.Stick: items.Stick(),
    items.Stone: items.Stone(),
    items.Club: items.Club(),
    items.Dagger: items.Dagger()
  }

  weaponReturned = False

  # i is for every weapon in the dictionary
  # Checks if the enemy is allowed to use the weapon, then rolls chance to recieve it
  while weaponReturned == False:
    for i in enemyWeapons:
      if ((i in allowed) and (random() < i.chanceToGet)):
        weaponReturned = True
        return enemyWeapons[i]


# Returns a random minor enemy
def getRandomEnemy():
  # Dictionary of enemies
  enemies = {
    Rat: Rat(),
    Spider: Spider(),
    UndeadSoldier: UndeadSoldier(),
    Goblin: Goblin(),
    Spirit: Spirit()
  }

  enemyReturned = False

  # Rolls chance to encounter wild enemies
  while enemyReturned == False:
    for i in enemies:
      if (random() < i.chanceToEncounter):
        enemyReturned = True
        return enemies[i]


# Set back to random encounter chance
def testEnemyEncounter(player):
  if random() < 1:
    encounterEnemy(player)

# Random enemy encounter, pass in class player
def encounterEnemy(player):
  # Enemy and player
  e = getRandomEnemy()
  p = player

  # Actions player can pick from, enemy will roll chance
  playerActions = ["attack", "cower", "run"]
  enemyActions = ["attack", "taunt"]

  # Keeps track of if combat is over and whose turn it is
  # Player plays on odd turns, enemy on even
  combatFinished = False
  turn = 1

  # Determines if player can escape enemy (use run option)
  def canEscape():
    escapeChance = 0.1 * (p.MAX_HEALTH / e.health)
    if random() < escapeChance:
      return True
    else:
      return False

  # Dialogue for encounter start
  clearScreen()
  try:
    printSlow("you have encountered a wild " + e.name + " wielding " + e.weapon.name + "\n")
  except AttributeError: # Enemy isn't capable of weapon (rat, spider, etc...)
    printSlow("you have encountered a wild " + e.name + "\n")
  sleep(1)
  printSlow("what will you do?\n\n")

  # While the enemy and player are alive
  while combatFinished == False:
    if turn % 2 == 1: # if turn is odd (player action)
      while True:
        # Print the players options and get input
        print(playerActions[0] + ",", playerActions[1] + " or", playerActions[2] + "?")
        action = input("> ")
        # Act based upon input
        if action.lower() == playerActions[0]:
          print("attack")
          break
        elif action.lower() == playerActions[1]:
          print("cower")
          break
        elif action.lower() == playerActions[2]:
          if canEscape() == True:
            printSlow("you managed to escape...\n\n")
            combatFinished = True
          else:
            printSlow("you counld't get away\n\n")
            turn += 1
          break
        inputError(action)
    
    elif turn % 2 == 0: # if turn is even (enemy action)
      # Roll random to determine what enemy will do



      turn += 1
        
  print("combat done")

      




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
  chanceToEncounter = 1/10

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
    items.Stick,
    items.Stone,
    items.Club
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
    items.Stick,
    items.Stone,
    items.Dagger
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
