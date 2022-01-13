#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.

import main
import page1
import os
import sys
mistakesleft = 6

def incorrect(letter):
  incorrect_list = []
  incorrect_list.append(letter)
  page1.mistakesleft -= 1
  print("Sorry, that letter isn't in the word. You have", main.mistakesleft, "mistakes remaining. The letters you've guessed incorrectly are:", *incorrect_list)
  print("Spaces left in word:")
  for i in range(1, 2):
    print("_ " * len(main.spaces_list))
  if main.mistakesleft == 0:
    print("You've reached the maximum number of tolerable mistakes. Every normal person now despises you. Goodbye!")
    os.system("clear")
    sys.exit()