# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        self.items = items

    def add_items_to_room(self, items):
        self.items = []
        if len(items) == 1:
            items.append(items[0])
        else:
            for item in items:
                self.items.append(item)

    def return_item_to_room(self, item):
        self.items.append(item)
        print(f"{item.name} returned to room")

    def remove_item_from_room(self, item):
        for i in self.items:
            if item == i.name:
                self.items.remove(i)
                print(f"{item} removed from {self.name}")
                break
            else:
                print(f"Item not found")

    def possible_moves(self):
        moves = []
        if self.n_to is not None:
            moves.append('n')
        if self.s_to is not None:
            moves.append('s')
        if self.e_to is not None:
            moves.append('e')
        if self.w_to is not None:
            moves.append('w')
        return ", ".join(moves)

    def get_items(self):
        room_items = []
        for item in self.items:
            room_items.append(item.name)
        return ", ".join(room_items)

    def __str__(self):
        room_msg = f"\n{self.name}\n\n"
        room_msg += f"{self.description}\n\n"

        if len(self.possible_moves()) > 0:
            room_msg += f"The possible moves are: {self.possible_moves()}\n\n"
        if len(self.items) > 0:
            room_msg += f"You can see a {self.get_items()}"
        return room_msg
