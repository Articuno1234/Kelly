try:
  import sys
  import os
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
  
def user_boot():
  print("                                                   \n"
        "                                                   \n"
        "                                                   \n"
        "                                                   \n"
        "                                                   \n"
        "                                                   \n"
        "                                                   \n"
        "---------------------------------------------------\n"
        "Start |                                            \n"
        "---------------------------------------------------\n")
  choice = user_choice()
  if choice == "start":
    user_boot()
    print("Start comming soon...")
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
