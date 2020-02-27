""" Simple class to encapsulate room functionality """

class Room(object):
    def __init__(self, roomconfig):
        self.name = roomconfig.name
        self.description = roomconfig["description"]
        self.options = roomconfig["options"].splitlines()
        self.decisions = roomconfig["decisions"].splitlines()
        self.needsitem = roomconfig["needsitem"] if "needsitem" in roomconfig else None
        self.noitem = roomconfig["noitem"] if "noitem" in roomconfig else None
        self.inventory = roomconfig["inventory"] if "inventory" in roomconfig else None

    """
    Play logic:
        If room is just to add inventory, do that and jump to next room
        Else if room requires an item and you don't have it, jump to noitem room
        Else print description, read option and verify, jump to room from decision
    """
    def play(self, player):
        # If room is just for inventory, add it and move on
        if inventory:
            player.inventory.append(inventory)
            return self.decisions[0]
        # If this room requires an item to give you options, skip to next room if you don't have it
        if self.needsitem and not self.needsitem in player.inventory:
            return self.noitem
        # Otherwise just play the room normally
        print(self.description)
        #read option choice
        #pick next room from decisions
        return nextroom
