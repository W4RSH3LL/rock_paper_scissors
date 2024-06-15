#!/usr/bin/python3

import random

# Defining the ASCII art of RPS for computer
computer_rock = '''
    _______
---'   ____)
      (_____)
computer(_____)
      (____)
---.__(___)
'''
computer_paper = '''
     _______
---'    ____)____
           ______)
computer  _______)
         _______)
---.__________)
'''

computer_scissors = '''
    _______
---'   ____)____
          ______)
computer__________)
      (____)
---.__(___)
'''

# Defining the ASCII art of RPS for user
user_rock = '''
       _______
  (____   '---
 (_____)
 (_____) player
  (____)
   (___)__.---
'''

user_paper = '''
      _______
  __(    '---
 (______
(_______ player
 (_______
   (__________.---
'''

user_scissors = '''
       _______
  ____(    '---
 (______
(__________ player
      (____)
       (___)__.---
'''

# Getting user input
user_input = int(input("Please enter 0 for Rock, 1 for Paper, 2 for Scissors\n[+] Choice > "))

# Associating the number selected with RPS
if user_input == 0:
    user_choice = user_rock
elif user_input == 1:
    user_choice = user_paper
elif user_input == 2:
    user_choice = user_scissors
else:
    print("[!] Error! Please enter a valid number! [!]")
    exit()

# Computer selecting a randint
random_number = random.randint(0, 2)
random_choice = ""

if random_number == 0:
    random_choice = computer_rock
elif random_number == 1:
    random_choice = computer_paper
elif random_number == 2:
    random_choice = computer_scissors
else:
    print("Error on selection!")
    exit()

# Comparing selections and determining the winner
if user_input == random_number:
    result = "It's a tie!"
elif (user_input == 0 and random_number == 2) or (user_input == 1 and random_number == 0) or (user_input == 2 and random_number == 1):
    result = "Player Wins!"
else:
    result = "Player loses!"

# Merging the ASCII art side by side
merged_art = ""
user_lines = user_choice.split('\n')
computer_lines = random_choice.split('\n')

for user_line, computer_line in zip(user_lines, computer_lines):
    merged_art += f'{computer_line:<40} {user_line}\n'

print(merged_art)
print(result)