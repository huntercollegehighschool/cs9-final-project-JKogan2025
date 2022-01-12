#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.

import main

def incorrect(letter):
  print("Sorry, that letter isn't in the word. You have", main.mistakesleft, "mistakes remaining. The letters you've guessed incorrectly are:", main.incorrect_list)
  print("Spaces left in word:")
  for i in range(1, 2):
    print("_ " * len(main.spaces_list))
  if main.mistakesleft == 0:
    print("You've reached the maximum number of tolerable mistakes. Every normal person now despises you. Goodbye!")
    import os
    import sys
    os.system("clear")
    sys.exit()