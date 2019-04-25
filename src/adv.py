from room import Room
from player import Player
from item import Item
# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

outsideItems = [
    Item(name="skull", description="Looks like it could be human"),
    Item(name="key", description="An old long key"),
    Item(name="letter", description="A letter that reads. 'It is done. No one will find it now.'"),
]

foyerItems = [
    Item(name="knife", description="A rusty knife"),
    Item(name="flashlight",
         description="A flickering flashlight. The battery may be going dead."),
    Item(name="pen", description="A dusty pen")
]


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Add items to rooms
# room['outside'].add_items(outsideItems)
# room['foyer'].add_items(foyerItems)

# room['outside'].possible_moves()
# room['foyer'].possible_moves()

# print('\n***OUTSIDE ITEMS***')
# for item in room['outside'].items:
#     print(item)

# print('\n***Foyer ITEMS***')
# for item in room['foyer'].items:
#     print(item)

# print(room['outside'].items)

#
# Main
#


# print(f"Player name: {player.name} \nCurrent Room: {player.current_room}")
# print(player.current_room.n_to)
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player = Player('Nate', room['outside'])

while True:

    # print(f"\n{player.name} approaches the {player.current_room.name}...")

    if player.current_room == room['outside']:
        print(player.current_room)
        cmd = input("\n\n-> Type 'n' to head into the Foyer:  ")
        if cmd == 'n':
            player.current_room = room['foyer']
        elif cmd != 'n' or cmd != 'q':
            print("**Please input 'n' to head into the Foyer. Or 'q' to quit.**")
    if player.current_room == room['foyer']:
        print(f"\n{player.name} walks into the {player.current_room.name}...\n")
        print(f"{player.current_room}\n")
        # print(
        #     f"To the north is the the {player.current_room.n_to.name}.\nTo the south is the {player.current_room.s_to.name}.\nTo the east is the {player.current_room.e_to.name}.\n")
        print("Which way way will he go?\n")
        cmd = input("What will he do: ")
        if cmd == 'n':
            player.current_room = player.current_room.n_to
        elif cmd == 's':
            player.current_room = player.current_room.s_to
        elif cmd == 'e':
            player.current_room = player.current_room.e_to
    if player.current_room == room['overlook']:
        print(player.current_room)
        cmd = input("What will he do: ")
        if cmd == 's':
            player.current_room = player.current_room.s_to
    if player.current_room == room['narrow']:
        print(player.current_room)
        cmd = input("What will he do: ")
        if cmd == 'w':
            player.current_room = player.current_room.w_to
        elif cmd == 'n':
            player.current_room = player.current_room.n_to
    if player.current_room == room['treasure']:
        print(player.current_room)
        cmd = input("What will he do: ")
        if cmd == 's':
            player.current_room = player.current_room.s_to
    if cmd == "q":
        break
