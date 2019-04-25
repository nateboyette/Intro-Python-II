# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room=None, items=None):
        self.name = name
        self.current_room = starting_room
        self.items = items
