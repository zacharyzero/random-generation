#This script is used to generate a random secure password

#Import the random and string modules from Python
import random
import string

#Create function that generates a random password
def generate_password(length=16):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password

#Call the generate_password function using a while loop
while True:
  choice = input("Press 1 to generate a random secure password!\n")
  if choice == "1":
    length_input = input("\nEnter the desired password length (press Enter to use default 16):\n")
    if length_input == "":
      length = 16
    elif length_input.isdigit():
      length = int(length_input)
    else:
      print("Invalid input. Please enter a valid number.")
      continue
    print(f"\nYour generated password: {generate_password(length)}\n")
  else:
    print("\nInvalid option. Please try again.\n")
