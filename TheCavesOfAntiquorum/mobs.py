# NPC database

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
    