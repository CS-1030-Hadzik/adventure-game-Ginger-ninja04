"""
Adventure Game
Author: Alexander Price
Version 1.0
Description:
This is a text-based adventure game where the player makes choices to navigate through a mysterious forest.
"""


# create clear
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome_player():
    clear()
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")
    name = input("Whats your name, adventurer? ")
    clear()
    print(f"Welcome, {name}! Your journey begins here...")

def describe_area():
    starting_area = """
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the unknown...
    """

    print(starting_area)

    decision = input("Do you wish to take the path? (yes or no): ").lower()
    clear()
    if decision == "yes":
        print(f"Brave choice, {name}! You step onto the path and venture forward.")
    elif decision == "no":
        print("oops")
    else:
        print("Confused, you stand still, unsure of what to do.")

welcome_player()