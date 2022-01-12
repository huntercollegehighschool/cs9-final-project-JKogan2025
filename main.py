"""
Name(s): Joseph Kogan
Name of Project: Python 1 (Hangman)
"""

#Write the main part of your program here. Use of the other pages is optional.

from time import sleep
import page1

print("Welcome to the best hangman game in the world!")
sleep(1.5)
print("The rules are simple: the number of letters in the generated word will be represented on the screen as dashes, and you will have to guess each letter to win! If at any time you want to guess the word in it's entirety you may do so, but you may only have one guess. If that guess is wrong, you lose. Beware, if you make six letter mistakes, you lose.")
sleep(1.5)
print("Without further ado, good luck!")

list_a = ["conspicuous", "alligator", "connoisseur", "detrimental", "vivacious", "presidential", "collection", "lackadaisical", "fuchsia", "thumbscrew", "lymph", "marquis"]

x = int(input("Choose an integer from 1-12 to generate a random word for hangman: "))
x -= 1
word = list_a[x]
spaces_list = list(word)

mistakesleft = 6

print("Spaces left in word:")
for i in range(1, 2):
  print("_ " * len(spaces_list))

def correct(letter):
  print("That's correct!")
  print("Spaces left in word:")
  for i in range(0, len(spaces_list)):
    if spaces_list[i] == letter:
      print(letter, "", sep = "")
    elif spaces_list[i] != letter:
      print("_ ", sep = "")
    elif i == len(spaces_list):
      print("_")
  while letter in spaces_list:
    spaces_list.remove(letter)

incorrect_list = []

def guesser(letter):
  letter = input("Type your next letter guess here: ")
  joinedspaces_list = ''.join(spaces_list)
  if letter in spaces_list:
    guesser(letter)
  elif letter == joinedspaces_list:
    print("Woah, you guessed the full word, and without guessing each letter! The Force must be strong with this one. I must tell my master...")
    import os
    import sys
    os.system("clear")
    print("Hangman program has been terminated. Instructions to follow.")
    sys.exit()
  else:
    mistakesleft -= 1
    page1.incorrect(letter)
    incorrect_list.append(letter) 

l1 = input("Type your first letter guess here: ")
if l1 in spaces_list:
  guesser(l1)
else:
  mistakesleft -= 1
  page1.incorrect(l1)
  incorrect_list.append(l1)

while mistakesleft != 0 and len(spaces_list) != 0:
  guesser


#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
