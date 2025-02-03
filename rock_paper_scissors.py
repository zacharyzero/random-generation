#This script is my solution for Codecademy's rock, paper, scissors project using Python
"""This program will prompt the user to select rock, paper, or scissors. It will then randomly select its own choice and compare with the user to determine a winner."""

#Import Python's random module
from random import randint

#Assign values for options in the game of rock, paper, scissors
options = ["ROCK", "PAPER", "SCISSORS"]

#Assign values to the message variable for the outcome of the game
message = {
  "tie": "Yawn, it's a tie!",
  "won": "Yay, you won!",
  "lost": "Aww, you lost!"
}

#Define the function to determine the winner of rock, paper, scissors
def decide_winner(user_choice, computer_choice):
  print("You selected: %s" % user_choice)
  print("Computer selected: %s" % computer_choice)

  if user_choice == computer_choice:
    print (message["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
    print (message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
    print (message["won"])
  elif user_choice == options[2] and computer_choice == options[1]:
    print (message["won"])
  else:
    print (message["lost"])

#Define the function for playing rock, paper, scissors
def play_RPS():
  print("Rock, Paper, or Scissors?")
  user_choice = input("\nEnter Rock, Paper, or Scissors:\n")
  user_choice = user_choice.upper().strip()
  if user_choice not in options:
        print("Invalid choice. Please select Rock, Paper, or Scissors.")
        return play_RPS()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)

#Call the function play_RPS to start the game
play_RPS()
