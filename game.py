# create clear
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

#Ask for player name
print("Welcome to the Adventure Game!")  
print("Your journey begins here...")
name = input("Whats your name, adventurer? ")
print("Hello,",name)

print(f"Welcome, {name}! Your journey begins here...")

clear()

#Describe the starting area
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""

print(starting_area)

decision = input("Do you wish to take the path? (yes or no): ").lower()

if decision == "yes":
    print(f"Brave choice, {name}! You step onto the path...")
elif decision == "no":
    print("Lmao loser hahaha")
else:
    print("Confused, you stand still, unsure of what to do.")