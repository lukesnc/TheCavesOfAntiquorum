# Act 2

# KEY FEATURES
# slow typed out text
# inventory (player can't access but it's there)

# includes
from TheCavesOfAntiquorum import items, const
from TheCavesOfAntiquorum.player import Player
from TheCavesOfAntiquorum.helpers import clearScreen, inputError, printSlow, printVerySlow, startAct

from time import sleep

# Creates an object of player
p1 = Player()
dynamite = 0

def writeDynamiteToSave():
  # Write explosive to save
  save = open(const.SAVE_PATH, 'a')
  if dynamite == 1:
    save.write("DYNAMITE=1\n")
  else:
    save.write("DYNAMITE=0\n")
  save.close()

  printSlow("\nSave file updated.\n")
  sleep(1)

# Final text and starts act 3
def endOfAct2():
  writeDynamiteToSave()
  sleep(2)
  print("\ndespite the cave seeming to change on its own, you find a way back to the rubble")
  sleep(1)
  print("the rubble seems more built up, almost no light is coming through at this point")
  sleep(1)
  printSlow("\na way back through may not be possible...\n")
  sleep(3)

  # Deletes object of player
  global p1
  del p1
  startAct(3)

# Player will find explosive on the ground
def findExplosive():
  global dynamite
  dynamite = 1

  print("\nyou take a step back and hit your head")
  sleep(1)
  print("\"what the fuck\" you exclaim out loud")
  sleep(2)
  print("that wall was not there before, and the ceiling was definitely not that low\n")
  sleep(3)
  print("you turn around once more, this time you notice something on the ground\n")
  sleep(2)

  while True:
    print("inspect ground?")
    sleep(1)
    print("yes or no")
    option = input("> ")

    if option == "yes":
      print("you walk over and reach down\n")
      sleep(1)
      printSlow("picked up: " + items.Dynamite.name + "\n")
      sleep(1)
      print("you think you might be able to blow up the rubble and get back to the door with this")
      sleep(1)
      endOfAct2()
      break
    elif option == "no":
      print("you keep looking around\n")
      sleep(1)
      print("the cave keeps changing")
      sleep(3)
      print("the walls have been morphing")
      sleep(1)
      print("the paths have been changing\n")
      sleep(1)
      printSlow("what is going on?\n")
      sleep(3)
      
      print("you fall down, on your knees, trembling\n")
      sleep(1)
      print("you move your hands around and feel something, you grab it")
      sleep(1)
      printSlow("picked up: " + items.Dynamite.name + "\n")
      sleep(1)
      print("what do i need this for?")
      sleep(2)
      endOfAct2()
      break
    inputError(option)

def jump():
  sleep(3)
  print("you prepare youself, and get ready to jump\n")
  sleep(2)
  print("you throw youself forward", end='')
  printSlow("...")
  sleep(1)
  print("\nbut your foot gets caught on a rock\n")
  sleep(3)
  print("you're dangling out over the ledge, staring down at the void")
  sleep(5)
  clearScreen()
  printSlow("the blackness is calling out to you, urging you forward\n")
  sleep(2)
  print("you feel a deep rumble throughout the cavern\n")
  sleep(6)
  print("you scramble to get your grip again")
  sleep(1)
  print("hoisting youself back onto the ledge you just tried to throw yourself off of\n")
  sleep(4)
  
  print("you back up\n")
  sleep(1)
  while True:
    print("try again or go back")
    option = input("> ")

    if option == "try" or option == "try again":
      print("you back up and breathe, preparing to go again")
      sleep(3)
      print("but something is different\n")
      sleep(1)
      print("the tunnels seem off again")
      sleep(3)
      findExplosive()
      break
    elif option == "back" or option == "go back":
      print("you decide jumping off of a cliff might have been a bad idea")
      sleep(2)
      print("you turn to head back")
      sleep(2)
      findExplosive()
      break
    inputError(option)

def jumpOrBack():
  while True:
    print("jump or go back")
    option = input("> ")

    if option == "jump":
      jump()
      break
    elif option == "go back" or option == "back":
      pastThicket()
      break
    inputError(option)

def pastThicket():
  print("you keep crawling for a bit")
  sleep(1)
  print("\nyour hands slip and you realize your hanging out over a large ravine")
  sleep(1)
  print("you scramble to get your grip, and do, but there is no easy way down")
  sleep(1)
  print("\nit's too dim to tell, but it sounds like there could be water below you\n")
  sleep(1)
  while True:
    print("throw something or jump")
    option = input("> ")

    if option == "throw something" or option == "throw":
      global p1
      print("you fumble around in your pockets for a bit", end='')
      printVerySlow("...")
      sleep(1)
      if items.UselessKey.ID in p1.inventory:
        print("\nyou feel the " + items.UselessKey.name + " that you picked up earlier")
        sleep(1)
        while True:
          print("\nthrow it?\nyes or no")
          option2 = input("> ")

          if option2 == "yes":
            print("you decide throwing the key is the best option to test for water")
            sleep(1)
            print("\nyou throw the key", end='')
            printVerySlow(".........")
            sleep(2)
            p1.inventory.remove(items.UselessKey.ID)
            print("\n\nyou hear a splash")
            sleep(3)
            print("the water seems safe to land in\n")
            sleep(2)
            jumpOrBack()
            break
          elif option2 == "no":
            print("you decide against throwing the key")
            sleep(1)
            print("there aren't any other options\n")
            sleep(1)
            jumpOrBack()
            break
          inputError(option2)
        break
      else:
        print("\nyou can't seem to find anything to throw")
        sleep(1)
        print("and you figure throwing the lamp might be a bad idea\n")
        sleep(1)
        print("you don't really have any other options\n")
        sleep(1)
        jumpOrBack()
    elif option == "jump":
      jump()
      break
    inputError(option)

def differentArea():
  print("you crawl back the way you came, but something's different\n")
  sleep(1)
  print("the walls seem different")
  sleep(1)
  print("the thicket is gone")
  sleep(3)
  print("\nthis doesn't make sense")
  sleep(1)
  print("your heart rate picks up\n")
  sleep(2)
  while True:
    print("look around or go back")
    option = input("> ")

    if option == "look" or option == "look around":
      print("you stop for a second and really look around\n")
      sleep(3)
      print("the walls are deformed, spikes coming in on all sides")
      sleep(2)
      print("there's a wretched smell hanging in the air")
      sleep(2)
      print("it seems like the cave might close in on you at any second\n")
      sleep(3)
      printSlow("you start to panic\n\n")
      sleep(3)
      while True:
        print("keep looking or go back")
        option2 = input("> ")

        if option2 == "keep looking" or option2 == "keep":
          sleep(2)
          print("the more you look aroud the more terrified you become")
          sleep(2)
          print("you try to keep crawling forward but your arms give out\n")
          sleep(2)
          printSlow("your vision goes black......\n")
          sleep(6)
          clearScreen()
          inspectThicket()
          break
        elif option2 == "go back" or option2 == "back":
          sleep(1)
          print("you decide to head back before anything gets any wierder")
          sleep(1)
          print("quickly turning around you manage to bump your head a bit, but you push on\n")
          jump()
          break
        inputError(option2) 
      break
    elif option == "back":
      print("you rub your eyes, you must be seeing things")
      sleep(1)
      print("you turn back around and go the other way towards the sound of water")
      sleep(2)
      jump()
      break
    inputError(option)

def inspectThicket():
  print("it's sharp through there\n")
  sleep(1)
  print("do i really need to crawl through...")
  sleep(1)

  while True:
    print("\nbe brave or cower")
    option = input("> ")

    if option == "be brave" or option == "brave":
      sleep(1)
      print("it hurts")
      sleep(1)
      print("\nthe light gets stronger... it's blinding")
      sleep(2)
      print("you emerge into a tight tunnel, the walls practically suffocating you")
      sleep(1)
      print("you see only one way forward")
      sleep(1)

      while True:
        print("\nkeep going or go back")
        option2 = input("> ")
        
        if option2 == "keep going":
          pastThicket()
          break
        elif option2 == "go back" or option2 == "back":
          differentArea()
          break
        inputError(option2)
      break
    elif option == "cower":
      sleep(1)
      print("\nthe light beyond the thicket screams")
      sleep(1)
      print("you close your eyes but its still blinding\n")
      sleep(1)
      printSlow("you can't think\n")
      sleep(3)
      clearScreen()
      lookAround()
      break
    inputError(option)

# Story of act 2 begins here
def lookAround():
  print("you glance around frantically, your heart pounding")
  sleep(1)
  print("you survived the tumbling rocks, but the way back is blocked")
  sleep(1)
  print("you'll need to find a way back")
  sleep(1)

  while True:
    print("\nlook around or hide")
    option = input("> ")

    if option == "look around" or option == "look":
      print("you come to your senses and analyze your surroundings")
      sleep(1)
      print("\nthe tunnel is dusty, making it hard to breath")
      sleep(1)
      print("there is a massive thiccet in front of you, there are dead rats embedded within")
      sleep(1)

      while True:
        print("\ninspect thicket or keep looking")
        option2 = input("> ")

        if option2 == "inspect thicket" or option2 == "thicket" or option2 == "inspect":
          inspectThicket()
          break
        elif option2 == "keep looking":
          print("this time you notice a faint light coming through the brush ")
          sleep(1)
          print("the way back isn't an impossible route, but you'll definitely need something to move the rockfall\n")
          sleep(3)
          print("you move on to the thicket...")
          inspectThicket()
          break
        inputError(option2)
      break

    elif option == "hide":
      sleep(3)
      print("you ball up against the wall of the cave")
      sleep(1)
      print("gripping your legs tight to your body")
      sleep(3)
      clearScreen()
      printVerySlow("you're pathetic\n")
      sleep(6)
      printSlow("\nnow get moving")
      sleep(2)
      clearScreen()
      sleep(2)
      lookAround()
      break
    inputError(option)

# First function of act 2, begins the second chapter of story
def start():
  clearScreen()
  printSlow("Welcome to Act 2 of The Caves of Antiquorum\n")
  printSlow("Press ENTER to continue...")
  input()
  clearScreen()
  sleep(3)
  lookAround()
