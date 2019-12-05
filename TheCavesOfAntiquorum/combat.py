# File containing the class for the combat system

# includes
from TheCavesOfAntiquorum.helpers import clearScreen, printSlow, inputError
from TheCavesOfAntiquorum import mobs as m

from time import sleep
from random import random

class CombatSystem():
  # Consts
  ENEMY_ATTACK_CHANCE = 3/4 # Chance enemy's random combat action will be "attack"

  # Set back to random encounter chance
  def testEnemyEncounter(self, player, rate):
    if random() < rate:
      self.encounterEnemy(player)

  # Returns a random minor enemy
  def getRandomEnemy(self):
    # Dictionary of enemies
    enemies = {
      m.Rat: m.Rat(),
      m.Spider: m.Spider(),
      m.UndeadSoldier: m.UndeadSoldier(),
      m.Goblin: m.Goblin(),
      m.Spirit: m.Spirit()
    }

    enemyReturned = False

    # Rolls chance to encounter wild enemies
    while enemyReturned == False:
      for enemy in enemies:
        if (random() < enemy.chanceToEncounter):
          enemyReturned = True
          return enemies[enemy]

  # Random enemy encounter, pass in class player
  def encounterEnemy(self, player):
    # Enemy and player
    e = self.getRandomEnemy()
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
      escapeChance = 0.13 * (p.MAX_HEALTH / e.health)
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
    except: # Enemy isn't capable of weapon (rat, spider, etc...)
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
            sleep(2)
            print("you curl up in fear")
            sleep(1)
            print("the enemy's gaze burning a hole through you\n")
            sleep(3)
            printSlow("you freeze\n")
            sleep(3)
            print("fear has taken hold of you\n")
            sleep(5)
            print("you snap out of it")
            sleep(2)
            print("but you feel something has changed")
            sleep(2)
            print("quite possibly in your favor\n")
            sleep(3)
            # Player's chance of critical hit increases
            p.critChance += 0.01
            break
          elif action.lower() == playerActions[2]:
            if canEscape() == True:
              printSlow("you managed to escape...\n\n")
              combatFinished = True
            else:
              printSlow("you couldn't get away\n\n")
            break
          inputError(action)
      
      if turn % 2 == 0: # if turn is even (enemy action)
        # Roll random to determine what enemy will do
        if random() < self.ENEMY_ATTACK_CHANCE: 
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
          
    p.critChance = p.DEFAULT_CRIT_CHANCE
    print("combat done")
