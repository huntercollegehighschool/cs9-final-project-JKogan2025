"""
Name(s): Joseph Kogan
Name of Project: Python 1 (Hangman)
"""

#Write the main part of your program here. Use of the other pages is optional.

from time import sleep
from page1 import mistakesleft
import os
import sys

print("Welcome to the best hangman game in the world!")
sleep(1.5)
print("The rules are simple: the number of letters in the generated word will be represented on the screen as dashes, and you will have to guess each letter to win! If at any time you want to guess the word in its entirety you may do so, but you may only have one guess. If that guess is wrong, you lose. Beware, if you make six letter mistakes, you lose.")
sleep(1.5)
print("Without further ado, good luck!")

list_a = ["conspicuous", "alligator", "connoisseur", "detrimental", "vivacious", "presidential", "collection", "lackadaisical", "fuchsia", "thumbscrew", "lymph", "marquis"]

sleep(2.5)
x = int(input("Choose an integer from 1-12 to generate a word for hangman: "))
x -= 1
spaces_list = list(list_a[x])
joinedspaces_list = ''.join(spaces_list)
incorrect_list = []

print("Spaces left in word:")
originaldashes_list = ["_ "]
for i in range(1, len(spaces_list)):
  originaldashes_list.append("_ ")
print(*originaldashes_list)

def incorrect(letter):
  print("Sorry, that letter isn't in the word. You have", mistakesleft, "mistakes remaining. The letters you've guessed incorrectly are:", *incorrect_list)
  print("Spaces left in word:")
  print(*originaldashes_list)
  if mistakesleft == 0:
    print("You've reached the maximum number of tolerable mistakes. Every normal person now despises you. Goodbye!")
    os.system("clear")
    sys.exit()
  letter = None

def correct(letter):
  while letter in spaces_list:
    indicestoreplace = []
    index = spaces_list.index(letter)
    indicestoreplace.append(index)
    spaces_list.pop(index)
  #letter_index = [z for z, x in enumerate(spaces_list) if x == letter]
  print("That's correct!")
  print("Spaces left in word:")
  #originaldashes_list = [letter if letter == letter_index else letter for letter in originaldashes_list]
  print(*originaldashes_list)
  letter = None

while mistakesleft != 0 and ''.join(originaldashes_list) != joinedspaces_list:
  letter = input("Type your letter guess here: ")
  if letter in spaces_list:
    correct(letter)
  elif len(letter) == 1 and letter not in spaces_list and len(incorrect_list) == 0:
    incorrect_list.append(letter)
    mistakesleft -= 1
    incorrect(letter)
  elif len(letter) == 1 and letter not in spaces_list and len(incorrect_list) > 0:
    incorrect_listletters = [",", letter]
    incorrect_list.extend(incorrect_listletters)
    incorrect_listletters = None
    mistakesleft -= 1
    incorrect(letter)
  elif len(letter) > 1 and letter != joinedspaces_list:
    print("That guess is incorrect, and the hangman program shall now be terminated.")
    sleep(2)
    sys.exit()
  elif letter == joinedspaces_list:
    print("Woah, you guessed the full word, and without guessing each letter! The Force is strong with this one. I must tell my master...")
    sleep(4)
    os.system("clear")
    print("Hangman program has been terminated. Instructions to follow.")
    sys.exit()

if ''.join(originaldashes_list) == joinedspaces_list:
  print("Great job! You guessed the word! If you would like to play again, simply re-run the program.")

''''
joinedoriginaldashes_list = ''.join(originaldashes_list)
while mistakesleft != 0 or joinedspaces_list != joinedoriginaldashes_list:
  '''

''''
from correct import dash_list
from incorrect import mistakesleft
'''


#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
