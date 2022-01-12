#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.

def guesser(letter):
  if letter in spaces_list:
    print("That's correct!")
    print("Spaces left in word:")
    for i in range(0, len(spaces_list)):
      if spaces_list[i] == letter:
        print(letter, "")
      else:
        print("_ ")
    while letter in spaces_list:
      spaces_list.remove(letter)