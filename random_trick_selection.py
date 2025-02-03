#This Python script generates a skateboarding trick to try

#Print the script's purpose
print("Generate a flatground skateboarding trick to try!\n")

#Import random module from Python
import random

#Create a predefined list of skateboarding tricks to attempt
trick_list = [
  "ollie",
  "nollie",
  "fakie ollie",
  "switch ollie",
  "backside pop shuv it",
  "fakie backside pop shuv it",
  "nollie frontside pop shuv it",
  "switch backside pop shuv it",
  "frontside pop shuv it",
  "fakie frontside pop shuv it",
  "switch frontside pop shuv it",
  "nollie backside pop shuv it",
  "frontside 180 ollie",
  "fakie frontside 180 ollie",
  "nollie backside 180 ollie",
  "switch frontside 180 ollie",
  "backside 180 ollie",
  "fakie backside 180 ollie",
  "nollie frontside 180 ollie",
  "switch backside 180 ollie",
  "kickflip",
  "fakie kickflip",
  "nollie kickflip",
  "switch kickflip",
  "heelflip",
  "fakie heelflip",
  "nollie heelflip",
  "switch heelflip",
  "varial kickflip",
  "fakie varial kickflip",
  "nollie varial kickflip",
  "switch varial kickflip",
  "varial heelflip",
  "fakie varial heelflip",
  "nollie varial heelflip",
  "switch varial heelflip",
  "360 flip",
  "fakie 360 flip",
  "nollie 360 flip",
  "switch 360 flip",
  "hardflip",
  "nollie hardflip",
  "switch hardflip",
  "fakie hardflip",
  "frontside 180 kickflip",
  "nollie backside 180 kickflip",
  "fakie frontside 180 kickflip",
  "switch frontside 180 kickflip",
  "backside 180 kickflip",
  "switch backside 180 kickflip",
  "fakie 180 backside kickflip",
  "nollie frontside 180 kickflip",
  "frontside 180 heelflip",
  "switch frontside 180 heelflip",
  "fakie frontside 180 heelflip",
  "nollie backside 180 heelflip",
  "backside 180 heelfliip",
  "fakie backside 180 heelflip",
  "switch backside 180 heelflip",
  "nollie frontside 180 heelflip",
  "backside bigspin",
  "switch backside bigspin",
  "fakie backside bigpsin",
  "nollie frontside bigspin", 
  "frontside bigspin",
  "switch frontside bigspin",
  "nollie backside bigspin",
  "fakie frontside bigspin", 
  "bigspin kickflip",
  "fakie bigspin kickflip",
  "nollie bigspin kickflip",
  "switch bigspin kickflip",
  "inward heelflip",
  "fakie inward heelflip",
  "nollie inward heelflip",
  "switch inward heelflip",
  "bigspin heelflip",
  "fakie bigspin heelflip",
  "switch bigspin heelflip",
  "nollie bigspin heelflip",
  "ollie north",
  "body varial",
  "pressure flip",
  "casper flip",
  "impossible",
  "fakie impossible",
  "nollie impossible",
  "switch impossible"
  "backside 360",
  "fakie backside 360",
  "nollie frontside 360",
  "switch backside 360",
  "frontside 360",
  "switch frontside 360",
  "nollie backside 360",
  "fakie frontside 360"
]

#Ask the user if they want to add any additional tricks to the list
custom_trick_selection = input("Do you want to add any tricks to the list? (yes/no):\n").strip().lower()

#User inputs what tricks they want to add
if custom_trick_selection == "yes":
  new_tricks = input("Enter the tricks you want to add, separated by commas:\n").split(",")
  trick_list.extend([trick.strip() for trick in new_tricks if trick.strip()])

#Select and print a flatground skateboarding trick to try
print(f"You should try to land this trick: {random.choice(trick_list)}")
