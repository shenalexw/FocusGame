# Author: Alexander Shen
# Date: 11/28/2020
# Description: Replicate Focus/Domination board game with the win condition of capturing 6 pieces.

class Player:
    """
    Player class represents blueprint to create a Player object.
    Stores the name and color according to player's tuple.
    Tracks the number of captured and reserved pieces.
    Can add a capture and reserve piece.
    Can return all parameters in init method.
    """

    def __init__(self, profile):
        """ Initializes the name and color of the player along with their captured and reserved pieces."""
        self._player_name = profile[0]
        self._player_color = profile[1].upper()
        self._capture = 0
        self._reserve = 0

    def add_capture(self):
        """ Adds a captured piece to the player's collection"""
        self._capture += 1

    def add_reserve(self):
        """ Adds a reserved piece to the player's collection."""
        self._reserve += 1

    def use_reserve(self):
        """ Subtracts a reserved piece from the player's collection."""
        self._reserve -= 1

    def get_name(self):
        """ Returns a player's name. """
        return self._player_name

    def get_color(self):
        """ Returns a player's color."""
        return self._player_color

    def get_capture(self):
        """ Returns the number of captured pieces in a player's collection."""
        return self._capture

    def get_reserve(self):
        """ Returns the number of reserved pieces in a player's collection."""
        return self._reserve


class FocusGame:
    """
    FocusGame class creates a blueprint to create a FocusGame object.
    Creates the board and player objects.
    establishes the turn which is always the first player.
    """

    def __init__(self, first, second):
        """ Initializes the player objects, the board, and the first turn."""
        self._first_player = Player(first)
        self._second_player = Player(second)
        self._turn = self._first_player
        self._board = [
            [["R"], ["R"], ["G"], ["G"], ["R"], ["R"]],
            [["G"], ["G"], ["R"], ["R"], ["G"], ["G"]],
            [["R"], ["R"], ["G"], ["G"], ["R"], ["R"]],
            [["G"], ["G"], ["R"], ["R"], ["G"], ["G"]],
            [["R"], ["R"], ["G"], ["G"], ["R"], ["R"]],
            [["G"], ["G"], ["R"], ["R"], ["G"], ["G"]]
        ]

    def which_player(self, player_name):
        """ Given the player's name, return the object."""
        if player_name.upper() == self._first_player.get_name().upper():
            return self._first_player
        else:
            return self._second_player

    def change_turn(self, player):
        """ Changes the player's turn"""
        if player == self._first_player:
            self._turn = self._second_player
        else:
            self._turn = self._first_player

    def show_pieces(self, location):
        """ Returns a list of pieces within a given a tuple."""
        return self._board[location[0]][location[1]]

    def show_captured(self, player):
        """ Returns player's number of captured pieces."""
        return self.which_player(player).get_capture()

    def show_reserve(self, player):
        """ Returns player's number of reserved pieces"""
        return self.which_player(player).get_reserve()

    def print_board(self):
        """ Prints the board"""
        for lines in range(6):
            print(self._board[lines])

    def move_piece(self, player, select, move, number_pieces):
        """
        Move the desired amount of pieces to a location.
        It will call the check function to see if any input parameters are invalid.
        If the inputs are correct, then it will proceed to move the piece.
        If the movement causes a stack over 5, then it will call overflow and reduce it down to 5.
        It will also check winning conditions before displaying successfully moved.
        """
        if self.check(player, select, move, number_pieces):
            player_profile = self.which_player(player)
            piece_select = self._board[select[0]][select[1]]
            bottom_place = len(piece_select) - number_pieces
            for num in range(number_pieces):
                bottom_piece = piece_select[bottom_place]
                self._board[select[0]][select[1]].pop(bottom_place)
                self._board[move[0]][move[1]].append(bottom_piece)
            if len(self._board[move[0]][move[1]]) > 5:
                self.overflow(player, move)
                if player_profile.get_capture() == 6:
                    return player_profile.get_name() + " Wins"
            return "successfully moved"

        else:
            return False

    def reserved_move(self, player, move):
        """
        Move a piece from the player's reserve onto an existing stack.
        It will append a piece to the stack if the player's reserve is > 0.
        It will then check to see if the player has won, if the stack is over 5.
        """
        try:
            if self._board[move[0]][move[1]]:
                pass
        except IndexError:
            return False
        if move[0] < 0 or move[1] < 0:
            return False

        player_profile = self.which_player(player)
        if player_profile.get_reserve() > 0 and player_profile == self._turn:
            self._board[move[0]][move[1]].append(player_profile.get_color())
            player_profile.use_reserve()
            self.change_turn(player_profile)
            if len(self._board[move[0]][move[1]]) > 5:
                self.overflow(player, move)
                if player_profile.get_capture() == 6:
                    return player_profile.get_name() + " Wins"
            return "successfully moved"
        else:
            return False

    def overflow(self, player, move):
        """
        If the stack is over 5, then it will loop until it is not greater than 5.
        The bottom piece will be removed and added to the correct counter based on the player of the current turn.
        """
        player_profile = self.which_player(player)
        piece_move = self._board[move[0]][move[1]]
        while len(self._board[move[0]][move[1]]) > 5:
            bottom_piece = piece_move[0]
            self._board[move[0]][move[1]].pop(0)
            if bottom_piece == player_profile.get_color():
                player_profile.add_reserve()
            if bottom_piece != player_profile.get_color():
                player_profile.add_capture()

    def check(self, player, select, move, number_pieces):
        """
        Returns False if given the wrong move.
        This function is used to cover all the ways the piece can cause an invalid location.
        The player cannot move diagonal.
        The player cannot move an empty location.
        The player cannot source from or move to any location outside of the board.
        The player cannot move a piece that is not their color.
        The player cannot move to a location that does not match the number of pieces to be moved.
        The player cannot move if it not their turn.
        The player cannot move an incorrect number of pieces.
        """
        try:
            if self._board[move[0]][move[1]] and self._board[select[0]][select[1]]:
                pass
        except IndexError:
            return False
        piece_select = self._board[select[0]][select[1]]
        player_profile = self.which_player(player)
        if move[0] < 0 or move[1] < 0 or select[0] < 0 or select[1] < 0:
            return False
        if move[0] != select[0] and move[1] != select[1]:
            return False
        if not piece_select:
            return False
        if piece_select[len(piece_select) - 1] != player_profile.get_color():
            return False
        if number_pieces != abs(move[0] - select[0]) and move[1] == select[1]:
            return False
        if number_pieces != abs(move[1] - select[1]) and move[0] == select[0]:
            return False
        if player_profile != self._turn:
            return False
        if number_pieces > len(self._board[select[0]][select[1]]) or number_pieces <= 0:
            return False

        self.change_turn(player_profile)
        return True
