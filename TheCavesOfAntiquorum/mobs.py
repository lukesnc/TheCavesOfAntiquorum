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

  # Checks if the enemy is allowed to use the weapon, then rolls chance to recieve it
  while weaponReturned == False:
    for weapon in enemyWeapons:
      if ((weapon in allowed) and (random() < weapon.chanceToGet)):
        weaponReturned = True
        return enemyWeapons[weapon]


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
    for enemy in enemies:
      if (random() < enemy.chanceToEncounter):
        enemyReturned = True
        return enemies[enemy]


# Set back to random encounter chance
def testEnemyEncounter(player, rate):
  if random() < rate:
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

  # Determine if anyone is dead
  def checkHealths(pH, eH):
    if pH < 1 or eH < 1:
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
  sleep(.5)

  # While the enemy and player are alive
  while not combatFinished:
    if turn % 2 == 1: # if turn is odd (player action)
      # Update displayed values
      print("\n-=HEALTH=-")
      print("player: " + str(p.health))
      print(e.name + ": " + str(e.health) + "\n")

      while True:
        # Print the players options and get input
        print(playerActions[0] + ",", playerActions[1] + " or", playerActions[2] + "?")
        action = input("> ")
        # Act based upon input
        if action.lower() == playerActions[0]:
          # Takes away enemy health based on players damage
          sleep(1)
          e.takeDamage(p.attack())
          # Check if someone is dead
          combatFinished = checkHealths(p.health, e.health)
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
          break
        inputError(action)
    
    if turn % 2 == 0: # if turn is even (enemy action)
      # Roll random to determine what enemy will do
      if random() < Enemy.ATTACK_CHANCE: 
        action = enemyActions[0]
      else:
        action = enemyActions[1]

      sleep(1)
      if action == enemyActions[0]: # Enemy attacks
        # Take away player's health based on enemy damage
        p.takeDamage(e.attack())
        # Check if someone is dead
        combatFinished = checkHealths(p.health, e.health)
      else:  # Enemy taunts
        print("the " + e.name + " is staring at you")
        sleep(1)
        print("it's mocking you")
        sleep(1)
        print("\nthe " + e.name + " says, ", end='')
        sleep(1)
        printSlow("\"" + e.tauntMsg + "\"\n\n")
        sleep(1)

    sleep(1)
    turn += 1
        
  print("combat done")

      




# ENEMIES 

# Main enemy class (ALL ENEMIES SHARE THESE FUNCTIONS AND ATTRIBUTES)
class Enemy(object):
  # Consts
  UNKILLABLE = 999 # Health value given to an unkillable enemy
  ATTACK_CHANCE = 3/4 # Chance enemy's random combat action will be "attack"

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
    try:
      print("the " + self.name + " swings their " + self.weapon.name)
    except AttributeError:
      print("the " + self.name + " attacks")
    sleep(1)
    printSlow("the " + self.name + " deals " + str(self.damage) + " damage\n\n")
    return self.damage

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
  chanceToEncounter = 0.01

  def __init__(self):
    super().__init__()
    self.health = self.UNKILLABLE
