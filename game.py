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

def welcome_player():
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")
    name = input("Whats your name, adventurer? ")
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

while True:
    decision = input("\t1. Look around the forest (search for useful items)\n"
                     "\t2. Talk to a traveler (look for a map)\n"
                     "\t3. Explore a nearby cave\n"
                     "\t4. Search for a hidden valley\n"
                     "\t5. Stay where you are\n"
                     "\tType i to view your inventory: ").lower()

    if decision == "1":
        # Search the forest for useful items (lantern)
        if not player1.has_lantern:
            print("You search the forest and find an old but working lantern.")
            add_to_inventory("lantern", player1)
            player1.has_lantern = True
        else:
            print("You look around again, but you don't find anything new. You already have a lantern.")

    elif decision == "2":
        # Talk to a traveler to get a map
        print("You talk to a friendly traveler near the road.")
        if not player1.has_map:
            print("The traveler gives you a worn map of the area.")
            add_to_inventory("map", player1)
            player1.has_map = True
        else:
            print("You already have a map, so the traveler just wishes you good luck.")

    elif decision == "3":
        # Explore a nearby cave (requires lantern)
        if player1.has_lantern:
            print("Your lantern lights the way as you step into the dark cave.")
            if "treasure" not in player1.inventory:
                add_to_inventory("treasure", player1)
                print("Deep inside, you discover a chest filled with treasure!")
            else:
                print("You've already collected the treasure from this cave.")
        else:
            print("It's too dark to enter the cave without a lantern. You decide to turn back.")

    elif decision == "4":
        # Search for a hidden valley (requires map)
        if player1.has_map:
            print("Using your map, you follow a faint trail through the trees.")
            print("You discover a hidden valley filled with strange plants.")
            if "rare herbs" not in player1.inventory:
                add_to_inventory("rare herbs", player1)
                print("You gather some rare herbs that might be useful later.")
            else:
                print("You've already gathered rare herbs from this valley.")
        else:
            print("You wander around, but without a map you can't find the hidden valley.")

    elif decision == "5":
        print("Confused, you stand still, unsure of what to do.")

    elif decision == "i":
        print(player1.inventory)

    else:
        print("That is not a valid choice.")
