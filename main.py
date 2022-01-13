"""
Name(s): Joseph Kogan
Name of Project: Python 1 (Hangman)
"""

#Write the main part of your program here. Use of the other pages is optional.

from time import sleep
import os
import sys

print("Welcome to the best hangman game in the world!")
sleep(1.5)
print("The rules are simple: the number of letters in the generated word will be represented on the screen as dashes, and you will have to guess each letter to win! If at any time you want to guess the word in it's entirety you may do so, but you may only have one guess. If that guess is wrong, you lose. Beware, if you make six letter mistakes, you lose.")
sleep(1.5)
print("Without further ado, good luck!")

list_a = ["conspicuous", "alligator", "connoisseur", "detrimental", "vivacious", "presidential", "collection", "lackadaisical", "fuchsia", "thumbscrew", "lymph", "marquis"]

sleep(2.5)
x = int(input("Choose an integer from 1-12 to generate a random word for hangman: "))
x -= 1
spaces_list = list(list_a[x])
mistakesleft = 6

print("Spaces left in word:")
originaldashes_list = ["_ " * len(spaces_list)]
print(*originaldashes_list)

def incorrect(letter):
  incorrect_list = []
  incorrect_list.append(letter)
  mistakesleft = 6
  mistakesleft -= 1
  print("Sorry, that letter isn't in the word. You have", mistakesleft, "mistakes remaining. The letters you've guessed incorrectly are:", *incorrect_list)
  print("Spaces left in word:")
  for i in range(1, 2):
    dog = "_ " * len(spaces_list)
    print(dog)
  if mistakesleft == 0:
    print("You've reached the maximum number of tolerable mistakes. Every normal person now despises you. Goodbye!")
    os.system("clear")
    sys.exit()

def correct(letter):
  dash_list = ["_ " * len(spaces_list)]
  print("That's correct!")
  print("Spaces left in word:")
  dash_list.pop(spaces_list.index(letter))
  dash_list.insert(spaces_list.index(letter), letter)
  print(*dash_list)

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

''''
from correct import dash_list
from incorrect import mistakesleft
'''
while mistakesleft != 0 or "_ " in dash_list ==  True:
  l1 = input("Type your letter guess here: ")
  letterinput(l1)
  l1 = None


#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
