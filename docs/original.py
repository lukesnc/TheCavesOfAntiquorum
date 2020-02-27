#The Caves of Antiquorum
import time
 
key1 = 0
 
def inspectdoor():
 time.sleep(1)
 print("you jiggle the knob")
 print("it requires a key")
 if key1 == 0:
   time.sleep(2)
   paths()
 elif key1 == 1:
   print("you insert the key")
 
def throughhole():
 time.sleep(1)
 print("the air gets noticeably colder, the howl ceases\n")
 time.sleep(1)
 print("it's very dark, you find yourself stumbling, however you can see a faint glow further on\n")
 time.sleep(1)
 print("keep going?\n")
 print("keep going or go back")
 option = input("> ")
 if option == "keep going":
   print("you come to a bend in the tunneling, a burning torch sits before you")
   print("pick it up?\n")
   print("pick it up or keep going")
   option2 = input("> ")
   if option2 == "pick it up" or "pick up":
     print("it surges through")
 if option == "go back" or "back":
   paths()
 
def paths():
 print("the path in front of you seeps cold air, and appears as a dark hole in the wall, there is a faint howl\n")
 time.sleep(2)
 print("maybe wind, maybe beast\n")
 time.sleep(2)
 print("the path behind is shut by a door\n")
 print("inspect door, through hole, back")
 option2 = input("> ")
 if option2 == "inspect door":
   inspectdoor()
 if option2 == "through hole":
   throughhole()
 if option2 == "back":
   roomsorpaths()
 
def roomsorpaths():
 print("describe paths or room?\n")
 print("paths or room")
 
 option = input("> ")
 if option == "room":
   print("the room is barren")
   print("the ceiling depicts some artistic endeavor\n")
   time.sleep(3)
   print("you can barely make out the hieroglyphics\n")
   time.sleep(2)
   print("are those... teeth?\n")
   roomsorpaths()
  
 if option == "paths":
   paths()
  
 
def lightit():
 print("you get up and look around")
 print("you're standing in the center of a stone room\n")
 time.sleep(3)
 print("there are two openings in the room, one behind you and one in front\n")
 roomsorpaths()
 
def start():
 print("press 1 to exit the game")
 print("you wake up, your head hurts\n")
 print("it's dark all around, but there is a small unlit lantern next to you, light it?\n")
 print("leave it or light it")
 option = input("> ")
 if option == "leave it":
   start()
 elif option == "light it":
   print("you're embraced by a comforting warmth\n")
   time.sleep(2)
   lightit()
 
start()
