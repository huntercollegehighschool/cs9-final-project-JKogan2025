#Use of this page is optional. If you use code here, make sure either import page4 or from page4 import * appear on your main.py page.
from main import spaces_list
from page3 import correct
import sys
import os
def letterinput(letter):
  joinedspaces_list = ''.join(spaces_list)
  if letter in spaces_list:
    correct(letter)
  elif len(letter) > 1 and letter == joinedspaces_list:
    print("That guess is incorrect, and the hangman program shall now be terminated.")
    sys.exit()
  elif letter == joinedspaces_list:
    print("Woah, you guessed the full word, and without guessing each letter! The Force is strong with this one. I must tell my master...")
    os.system("clear")
    print("Hangman program has been terminated. Instructions to follow.")
    sys.exit()