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