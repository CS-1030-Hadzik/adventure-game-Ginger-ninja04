"""
Adventure Game
Author: Alexander Price
Version 1.0
Description:
This is a text-based adventure game where the player makes choices to navigate through a mysterious forest.
"""

from Player import Player

import os
inventory = []

def clear():
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("")

def welcome_player():
    clear()
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")
    name = input("Whats your name, adventurer? ")
    clear()
    print(f"Welcome, {name}! Your journey begins here...")
    player = Player(name)
    return player, name

def describe_area(name, player):
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
        print (player.inventory)
    else:
        print("Confused, you stand still, unsure of what to do.")

def add_to_inventory(item, player):
    player.inventory.append(item)
    print("You picked up", item)

player1, name = welcome_player()

describe_area(name, player1)

while (True):
    decision = input("\t1. Take the left path into the dark woods\n"
                     "\t2. Take the right path towards the mountain pass\n"
                     "\t3. Stay where you are\n"
                     "\t4. Explore the Hidden Valley\n"
                     "\t5. Stay where you are\n"
                     "\tType i to view your inventory: ").lower()

    
    if decision == "2":
        print("You go towards the mountain pass")
        add_to_inventory("map", player1)
        player1.has_map = True
    elif decision == "3":
        if player1.has_lantern:
            print("You go into the dark cave")
            add_to_inventory("Treasure", player1)

    elif decision == "4":
        print("You go into The Hidden Valley with a bown of salad")
    elif decision == "5":
        print("Confused, you stand still, unsure of what to do.")
    elif decision == "i":
        print (player1.inventory)
    else:
        print("That is not a valid choice")

