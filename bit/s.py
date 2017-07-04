try:
  import sys
  import os
  import time
  import subprocess
  import random
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
  
def root_boot():
  clear_screen()
  print("Root Comming soon!\n"
        "Loading user_boot() instead")
  time.sleep(2)
  user_boot()
def user_boot():
  clear_screen()
  print("                                                   \n"
        "                                                   \n"
        "                                                   \n"
        "                                                   \n"
        "                                                   \n"
        "                                                   \n"
        "                                                   \n"
        "---------------------------------------------------\n"
        "Start |                                   | Update \n"
        "---------------------------------------------------\n")
  choice = user_choice()
  if choice == "start":
    user_boot()
  if choice == "update":
    subprocess.call(("git", "clone", "https://github.com/Articuno1234/Kelly"))
    clear_screen()
    print("Updates Complete!")
    print("Note : if it says Updates are complete and it hasn't\n"
          "Delete the old Kelly File and Update again!")
    print("Note : Use 'cd Kelly' and then 'python3 run.py' When exited!")
    print("Exiting...")
    time.sleep(2)
    sys.exit(1)
def boot():
  clear_screen()
  print("\n"
        "Kelly\n"
        "\n")
  print("Boot Options:\n"
        "root\n"
        "user\n")
  choice = user_choice()
  if choice == "root":
    root_boot()
  if choice == "user":
    user_boot()
