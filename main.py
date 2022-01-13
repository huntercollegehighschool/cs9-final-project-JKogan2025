"""
Name(s): Joseph Kogan
Name of Project: Python 1 (Hangman)
"""

#Write the main part of your program here. Use of the other pages is optional.

from time import sleep

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

print("Spaces left in word:")
originaldashes_list = ["_ " * len(spaces_list)]
print(*originaldashes_list)

import page3
import page4
import page1
while page1.mistakesleft != 0 or "_ " in page3.dash_list ==  True:
  l1 = input("Type your letter guess here: ")
  page4.letterinput(l1)
  l1 = None


#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
