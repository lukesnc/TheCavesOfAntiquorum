from configparser import ConfigParser
from room import Room, Decision
from player import Player

GAMEFILE = "C:\\Users\\tony\\Downloads\\rooms.cfg"

rooms = ConfigParser()
try:
    rooms.read(GAMEFILE)
except:
    print("Failed.")
    exit(1)

start = rooms["START"]["start"]
nextroom = rooms[start]
myguy = Player()

# This will loop until nextroom is None, meaning you died or won
while nextroom:
    room = Room(nextroom)
    nextroom = room.play(myguy)

print("Game over")
