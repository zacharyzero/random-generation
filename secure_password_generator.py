#This script is used to generate a random secure password

#Import the random and string modules from Python
import random
import string

#Create function that generates a random password
def generate_password(length=16):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password

while True:
  choice = input("Press 1 to generate a random secure password!\n")
  if choice == "1":
    print(f"\n\{generate_password()}\n")
  else:
    print("\nInvalid option. Please try again.\n")
