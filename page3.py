#Use of this page is optional. If you use code here, make sure either import page3 or from page3 import * appear on your main.py page.
from main import spaces_list
dash_list = ["_ " * len(spaces_list)]

def correct(letter):
  print("That's correct!")
  print("Spaces left in word:")
  dash_list.pop(spaces_list.index(letter))
  dash_list.insert(spaces_list.index(letter), letter)
  print(*dash_list)