# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room=None, items=[]):
        self.name = name
        self.current_room = starting_room
        self.items = items

    def player_move(self, direction):
        directions = ['n', 's', 'e', 'w']
        if direction not in directions and direction != 'q':
            print("**Invalid Input**")

        if direction == 'n':
            if self.current_room.n_to is not None:
                self.current_room = self.current_room.n_to
            else:
                print("**Move not allowed**")
        if direction == 's':
            if self.current_room.s_to is not None:
                self.current_room = self.current_room.s_to
            else:
                print("**Move not allowed**")
        if direction == 'e':
            if self.current_room.e_to is not None:
                self.current_room = self.current_room.e_to
            else:
                print("**Move not allowed**")
        if direction == 'w':
            if self.current_room.w_to is not None:
                self.current_room = self.current_room.w_to
            else:
                print("**Move not allowed**")

    def get_item(self, input):
        room_items = []
        item_found = False
        item_in_inventory = False

        for i in self.current_room.items:
            room_items.append(i.name)

        # check if the input contains any items in the room
        for i in room_items:
            if i in input:
                item_found = True

        for i in self.items:
            if i.name in input:
                item_in_inventory = True

        if item_in_inventory is True:
            print("Item already in inventory")
            return

        # breaks out of function if item isn't found
        if item_found is not True:
            print("Item not Found")
            return

        # If the item exists, add to player inventory and remove from the room
        for i in self.current_room.items:
            if i.name in input:
                self.items.append(i)
                self.current_room.remove_item_from_room(i.name)
                print(f"{i.name} added to inventory.")

    def drop_item(self, input):
        for i in self.items:
            if i.name in input:
                self.items.remove(i)
                print(f"{i.name} removed from inventory")
                self.current_room.return_item_to_room(i)

    def get_inventory(self):
        inventory_list = []
        for item in self.items:
            inventory_list.append(item.name)

        inventory = ", ".join(inventory_list)
        print(f"You currently have these items in your inventory: {inventory}")

    def player_action(self, input):
        player_input = input.split()
        directions = ['n', 's', 'e', 'w']

        if "get" in player_input:
            self.get_item(player_input)
        if 'take' in player_input:
            self.get_item(player_input)
        if 'drop' in player_input:
            self.drop_item(player_input)
        if input in directions:
            self.player_move(input)
        if 'i' in player_input:
            self.get_inventory()
