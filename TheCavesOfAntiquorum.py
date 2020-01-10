# Run this file to begin the game

import sys
    
if __name__ == '__main__':
  try: 
    if sys.argv[1] == '--original':
      from docs import original
  except:
    from TheCavesOfAntiquorum import main
  sys.exit()
