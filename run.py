try:
  import sys
  import os
  import subprocess
  import random
  import time
  from bit import t
  from bit import s
except ImportError:
  input("Error 1\n"
        "ImportError")
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
INTERACTIVE_MODE = not len(sys.argv) > 1  # CLI flags = non-interactive


def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
        
def user_choice():
    return input("> ").lower().strip()

def boot():
  bit = ["32", "64"]
  if IS_WINDOWS:
    print("Loading 64-Bit")
    time.sleep(2)
    t.boot()
  if IS_MAC:
    print("Loading 32-Bit")
    time.sleep(2)
    s.boot()
  else:
    print("Loading {}-Bit".format(random.choice(bit)))
    time.sleep(2)
    s.boot()
    
boot = boot()
print(boot)
