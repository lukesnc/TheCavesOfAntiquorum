# NPC database

from TheCavesOfAntiquorum import items
from TheCavesOfAntiquorum.helpers import getRandomEnemyWeapon
from random import randint

class TestEnemy:
  name = "bad boy"
  damage = 1

  def __init__(self):
    self.health = 3
    self.isAlive = True

    # Looping interaction
    while self.isAlive:
      self.attack()

  def attack(self):
    print("take damage somehow")
    
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
    self.weapon = getRandomEnemyWeapon()
    
  def attack(self):
    return self.weapon.damage

  def takeDamage(self, damage):
    self.health = self.health - damage

