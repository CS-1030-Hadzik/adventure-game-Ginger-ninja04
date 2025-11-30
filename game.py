"""
Adventure Game
Author: Alexander Price
Version 1.0
Description:
This is a text-based adventure game where the player makes choices to navigate through a mysterious forest.
"""

from Player import Player


def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What's your name, adventurer? ")
    print(f"Welcome, {name}! Your journey begins now...")
    return Player(name)

def describe_area(player):
    starting_area = """
    You find yourself in a dark forest.
    You see two paths ahead
    """

    print(starting_area)

    while True:
        decision = input("Do you wish to take the path? (yes, no or i for inventory): ").lower()
        if decision == "yes":
            print(f"Brave choice, {player.name}! You step onto the path and venture forward.")
            break
        elif decision == "no":
            print("Then why are you here?")
            exit()
        elif decision == "i":
            print(player.inventory)
        else:
            print("Confused, you stand still, unsure of what to do.")

def add_to_inventory(item, player):
    player.inventory.append(item)
    print(f"You picked up: {item}")

def explore_dark_woods(player):
    print("You step into the dark woods. The trees close in around you and the light fades.")
    if not player.has_lantern:
        print("You search the forest and find an old but working lantern.")
        add_to_inventory("lantern", player)
        player.has_lantern = True
    else:
        print("You look around again, but you don't find anything new. You already have a lantern.")


def explore_mountain_pass(player):
    print("You walk toward the mountain pass where a narrow road winds between steep cliffs.")
    print("You see a traveler resting beside the road.")
    if not player.has_map:
        print("The traveler gives you a worn map of the area.")
        add_to_inventory("map", player)
        player.has_map = True
    else:
        print("You already have a map, so the traveler just wishes you good luck.")


def explore_cave(player):
    print("You arrive at the mouth of a dark cave.")
    if player.has_lantern:
        print("Your lantern lights the way as you step into the dark cave.")
        if "treasure" not in player.inventory:
            add_to_inventory("treasure", player)
            print("Deep inside, you discover a chest filled with treasure!")
        else:
            print("You've already collected the treasure from this cave.")
    else:
        print("It's too dark to enter the cave without a lantern. You decide to turn back.")


def explore_hidden_valley(player):
    print("You push through thick undergrowth searching for a hidden valley.")
    if player.has_map:
        print("Using your map, you follow a faint trail through the trees.")
        print("You discover a hidden valley filled with strange plants.")
        if "rare herbs" not in player.inventory:
            add_to_inventory("rare herbs", player)
            print("You gather some rare herbs that might be useful later.")
        else:
            print("You've already gathered rare herbs from this valley.")
    else:
        print("You wander around, but without a map you can't find the hidden valley.")


player1 = welcome_player()

describe_area(player1)

while True:
    decision = input("\t1. Look around the forest (search for useful items)\n"
                     "\t2. Talk to a traveler (look for a map)\n"
                     "\t3. Explore a nearby cave\n"
                     "\t4. Search for a hidden valley\n"
                     "\t5. Stay where you are\n"
                     "\tType i to view your inventory: ").lower()

    if decision == "1":
        explore_dark_woods(player1)

    elif decision == "2":
        explore_mountain_pass(player1)

    elif decision == "3":
        explore_cave(player1)

    elif decision == "4":
        explore_hidden_valley(player1)

    elif decision == "5":
        print("Confused, you stand still, unsure of what to do.")

    elif decision == "i":
        print(player1.inventory)

    else:
        print("That is not a valid choice.")

