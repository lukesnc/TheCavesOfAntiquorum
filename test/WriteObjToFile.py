# Test file to write an object to a file
# Works!

import pickle
path = "test/testObj.obj"

class Ball:
  PI = 3.14

  def __init__(self):
    self.radius = float(input("Enter the radius of a ball: "))

    self.volume = self.getVolume()
  
  def getVolume(self):
    v = (4/3) * self.PI * (self.radius ** 3)
    return v


# Pass in object of class Player to save to a file
def saveObj(obj):
  global path

  with open(path, 'wb') as output:
    pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def openObj():
  global path

  with open(path, 'rb') as infile:
    afterObj = pickle.load(infile)

  print("Infile (multiplying volume by 2):")

  afterObj.volume = afterObj.volume * 2
  print(afterObj.volume)

if __name__ == "__main__":
  # Create object of ball
  b = Ball()
  print(b.volume)

  # Write it to file
  saveObj(b)

  # Open it back up
  openObj()
