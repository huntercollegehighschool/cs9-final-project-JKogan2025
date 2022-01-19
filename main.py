"""
Name(s): Joseph Kogan
Name of Project: Python 1 (Hangman)
NOTE: The rules that print at the beginning are formatted so that they print correctly on a full console screen, so it is recommended to play the game in fullscreen.
"""

#Write the main part of your program here. Use of the other pages is optional.

from time import sleep
import wordlistandmistakes
import os
import sys

z = 10
y = 10
iterations = 0

while z == y:
  iterations += 1
  if iterations == 1:
    sleep(1.5)
    print("Welcome to the best hangman game in the world!")
    sleep(1.5)
    print("The rules are simple: the number of letters in the generated word will be represented on the screen as dashes, and you will have to guess each letter to win! If \nat any time you want to guess the word in its entirety you may do so, but you may only have one guess. If that guess is wrong, you lose. Beware, if you make six \nletter mistakes, you lose.")
    sleep(4)
    print("Without further ado, good luck!")
  else:
    sleep(1.5)
    print("Let's recall the rules: the dashes on your screen represent letters, and you must guess each letter to win, while staying within the six incorrect letter guess \nlimit. At any time, you may guess the full word, but you will only have one guess in this scenario. Good luck!")
    sleep(4)

  sleep(1)
  word = int(input("Choose an integer from 1-15 to generate a word for hangman: "))
  word -= 1

  spaces_list = list(wordlistandmistakes.list_a[word])
  joinedspaces_list = ''.join(spaces_list)
  finalspaces_list = spaces_list.copy()
  for i in finalspaces_list:
    dog = finalspaces_list.index(i)
    finalspaces_list[dog] = i + " "
  incorrect_list = []
  guessed_letters = []
  print("Spaces left in the word:")
  originaldashes_list = ["_ "]
  for i in range(1, len(spaces_list)):
    originaldashes_list.append("_ ")
  print(*originaldashes_list)

  def incorrect(letter):
    guessed_letters.append(letter)
    if wordlistandmistakes.mistakesleft > 1:
      print("Sorry, that letter isn't in the word. You have", wordlistandmistakes.mistakesleft, "mistakes remaining. The letters you've guessed incorrectly are:", *incorrect_list)
      sleep(1)
      print("Spaces left in the word:")
      print(*originaldashes_list)
      letter = None
    elif wordlistandmistakes.mistakesleft == 0:
      print("You've reached the maximum number of allowed mistakes. Every normal person now despises you. Goodbye!")
      sleep(4)
      os.system("clear")
      sys.exit()
    else:
      print("Sorry, that letter isn't in the word. You have 1 mistake remaining. The letters you've guessed incorrectly are:", *incorrect_list)
      sleep(1)
      print("Spaces left in the word:")
      print(*originaldashes_list)
      letter = None

  def correct(letter):
    guessed_letters.append(letter)
    print("That's correct!")
    sleep(1)
    print("Spaces left in the word:")
    index = spaces_list.index(letter)
    originaldashes_list[index] = letter + " "
    print(*originaldashes_list)
    letter = None

  def alreadyguessed(letter):
    print("You've already guessed that letter, sorry.")
    sleep(1)
    print("Spaces left in the word:")
    print(*originaldashes_list)
    letter = None

  while wordlistandmistakes.mistakesleft != 0 and ''.join(originaldashes_list) != ''.join(finalspaces_list):
    letter = input("Type your letter guess or full word guess here: ")
    if letter in guessed_letters:
      alreadyguessed(letter)
    elif letter in spaces_list:
      correct(letter)
    elif len(letter) == 1 and letter not in spaces_list and len(incorrect_list) == 0:
      incorrect_list.append(letter)
      wordlistandmistakes.mistakesleft -= 1
      incorrect(letter)
    elif len(letter) == 1 and letter not in spaces_list and len(incorrect_list) > 0:
      incorrect_listletters = [",", letter]
      incorrect_list.extend(incorrect_listletters)
      incorrect_listletters = None
      wordlistandmistakes.mistakesleft -= 1
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
      


  if ''.join(originaldashes_list) == ''.join(finalspaces_list):
    x = input("Great job! You guessed the word! Enter 'yes' or 'no' to indicate whether you'd like to play again: ")
    if x == "yes" or x == "Yes":
      print("Okay! Let's restart the program...")
      spaces_list = None
      incorrect_list = None
      guessed_letters = None
      originaldashes_list = None
      mistakesleft = 6
      finalspaces_list = None
      incorrect_listletters = None
      letters = None
      sleep(2)
      os.system("clear")
    else:
      print("That's alright. Come back any time!")
      sleep(2)
      z += 1