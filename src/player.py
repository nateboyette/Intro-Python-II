# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room=None, items=None):
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
