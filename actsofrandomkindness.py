print("Generate a random act of kindness")

import random

#Create a predefined list of acts of random kindness
acts_of_kindness = [
  "Send an encouraging text to a friend.",
  "Donate to a local charity.",
  "Compliment a stranger.",
  "Help a neighbor with a chore.",
  "Buy a coffee for the person in line behind you.",
  "Donate old clothes to Goodwill.",
  "Bring in treats for your coworkers.",
  "Spend 30 minutes picking up litter.",
  "Spontaneously call a family member or friend to check how they're doing.",
  "Leave a positive review for a small business you love.",
  "Donate books to a local library.",
  "Volunteer as a mentor.",
  "Write a thank you letter to someone who has helped you.",
  "Leave quarters at the laundromat with a note for laundry",
  "Gift someone your favorite book",
  "Donate blood or plasma to those in need"
]

#Ask the user if they want to add their own acts of random kindness
custom_acts = input("Do you want to add your own acts of kindness? (yes/no): ")

#If the user's answer is yes, prompt them to input their own custom acts
if custom_acts == "yes":
  new_acts =input("Enter your acts of kindness, separated by commas: ").split(",")
  acts_of_kindness.extend([acts.strip() for acts in new_acts])

#Select and print a random act of kindness
print(f" <3 Today's Random Act of Kindness: {random.choice(acts_of_kindness)}") 
