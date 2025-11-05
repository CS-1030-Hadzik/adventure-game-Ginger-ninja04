"""
Adventure Game
Author: Alexander Price
Version 1.0
Description:
This is a text-based adventure game where the player makes choices to navigate through a mysterious forest.
"""


# create clear
import os
inventory = []


def clear():
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("Clear")

def welcome_player():
    clear()
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")
    name = input("Whats your name, adventurer? ")
    clear()
    print(f"Welcome, {name}! Your journey begins here...")
    return name

def describe_area():
    starting_area = """
    You find yourself in a dark forest.
    You see two paths ahead
    """

    print(starting_area)

    decision = input("Do you wish to take the path? (yes, no or i for inventory): ").lower()
    clear()
    if decision == "yes":
        print(f"Brave choice, {name}! You step onto the path and venture forward.")
    elif decision == "no":
        print("oops")
    elif decision == "i":
        print (inventory)
    else:
        print("Confused, you stand still, unsure of what to do.")

def add_to_inventory(item):
    inventory.append(item)
    print("You picked up", item)

name = welcome_player()

describe_area()
decision = input("/t1. Take the left path into the dark woods/n"
                 "/t2. Take the right path towards the mountain pass/n"
                 "/t3. Stay where you are/n"
                 "/Type i to view your inventory").lower()

