import unittest
from FocusGame import FocusGame


class Test(unittest.TestCase):

    def test_1(self):
        """ Test if the player can make a single move """
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        result = game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        self.assertEqual(result, "successfully moved")

    def test_2(self):
        """ Test to see if show_pieces displays the list of a stack """
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        result = game.show_pieces((0, 1))
        self.assertEqual(result, ['R', 'R'])

    def test_3(self):
        """ Test to see if showing the captured pieces returns 0 """
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        result = game.show_captured('PlayerA')
        self.assertEqual(result, 0)

    def test_4(self):
        """ Test to see if showing the reserved pieces returns 0 """
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        result = game.show_reserve('PlayerA')
        self.assertEqual(result, 0)

    def test_5(self):
        """ Test to see if making a reserved move without reserved pieces returns False """
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        result = game.reserved_move('PlayerA', (0, 0))
        self.assertFalse(result)

    def test_6(self):
        """ Test to see if moving out of turn will return False"""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        result = game.move_piece('PlayerB', (0, 2), (0, 1), 1)
        self.assertFalse(result)

    def test_7(self):
        """ Test to see if moving the wrong color stack will return False"""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        result = game.move_piece('PlayerA', (0, 2), (0, 1), 1)
        self.assertFalse(result)

    def test_8(self):
        """ Test to see if moving to a location not in the board will return false"""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        result = game.move_piece('PlayerA', (0, 0), (0, -1), 1)
        self.assertFalse(result)

    def test_9(self):
        """ Test to see if player name is case insensitive."""
        game = FocusGame(('Player_A', 'R'), ('PlayerB', 'G'))
        result = game.move_piece('player_a', (0, 0), (0, 1), 1)
        self.assertEqual(result, "successfully moved")

    def test_10(self):
        """ Test to see if color is case insensitive."""
        game = FocusGame(('PlayerA', 'r'), ('PlayerB', 'g'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        result = game._first_player.get_color()
        self.assertEqual(result, 'R')

    def test_11(self):
        """ Test to see if selecting a location not in the board will return false"""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        result = game.move_piece('PlayerA', (0, 7), (0, 0), 1)
        self.assertFalse(result)

    def test_12(self):
        """ Test to see if selecting an empty location will return false"""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        result = game.move_piece('PlayerA', (0, 0), (1, 0), 1)
        self.assertFalse(result)

    def test_13(self):
        """ Test to see if moving diagonal will return false"""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        result = game.move_piece('PlayerA', (0, 1), (1, 2), 1)
        self.assertFalse(result)

    def test_14(self):
        """ Test to see if moving a 1 piece from a 2 stack returns successfully moved."""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        result = game.move_piece('PlayerA', (0, 1), (1, 1), 1)
        self.assertEqual(result, "successfully moved")

    def test_15(self):
        """ Test to see if the the top of the stack was placed onto the moved location."""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        game.move_piece('PlayerA', (0, 1), (0, 0), 1)
        result = game.show_pieces((0, 0))
        self.assertEqual(result, ["R"])

    def test_16(self):
        """ Test to see if moving with wrong number of pieces return false"""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        result = game.move_piece('PlayerA', (0, 0), (0, 1), 2)
        self.assertFalse(result)

    def test_17(self):
        """ Test to see if selecting a location not in the board will return false"""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        result = game.move_piece('PlayerA', (10, 0), (0, 0), 1)
        self.assertFalse(result)

    def test_18(self):
        """ Test move sets to retrieve 1 reserve for first_player. Should return 1"""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        game.move_piece('PlayerA', (0, 1), (0, 3), 2)
        game.move_piece('PlayerB', (5, 1), (5, 3), 2)
        game.move_piece('PlayerA', (5, 2), (5, 3), 1)
        game.move_piece('PlayerB', (0, 2), (0, 3), 1)
        game.move_piece('PlayerA', (4, 5), (5, 5), 1)
        game.move_piece('PlayerB', (1, 5), (0, 5), 1)
        game.move_piece('PlayerA', (5, 5), (5, 3), 2)
        result = game.show_reserve('PlayerA')
        self.assertEqual(result, 1)

    def test_19(self):
        """ Test move sets to retrieve 1 reserve for second_player. Should return 1"""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        game.move_piece('PlayerA', (0, 1), (0, 3), 2)
        game.move_piece('PlayerB', (5, 1), (5, 3), 2)
        game.move_piece('PlayerA', (5, 2), (5, 3), 1)
        game.move_piece('PlayerB', (0, 2), (0, 3), 1)
        game.move_piece('PlayerA', (4, 5), (5, 5), 1)
        game.move_piece('PlayerB', (1, 5), (0, 5), 1)
        game.move_piece('PlayerA', (5, 5), (5, 3), 2)
        game.move_piece('PlayerB', (0, 5), (0, 3), 2)
        result = game.show_reserve('PlayerB')
        self.assertEqual(result, 1)

    def test_20(self):
        """ Test to see if splitting the stack will place the pieces in the correct order on a new stack."""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        game.move_piece('PlayerA', (0, 1), (0, 3), 2)
        game.move_piece('PlayerB', (5, 1), (5, 3), 2)
        game.move_piece('PlayerA', (5, 2), (5, 3), 1)
        game.move_piece('PlayerB', (0, 2), (0, 3), 1)
        game.move_piece('PlayerA', (4, 5), (5, 5), 1)
        game.move_piece('PlayerB', (1, 5), (0, 5), 1)
        game.move_piece('PlayerA', (5, 5), (5, 3), 2)
        game.move_piece('PlayerB', (0, 5), (0, 3), 2)
        game.move_piece('PlayerA', (5, 3), (3, 3), 2)
        result = game.show_pieces((3, 3))
        self.assertEqual(result, ['R', 'G', 'R'])

    def test_21(self):
        """ Test to see if reserved move will return successfully moved."""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        game.move_piece('PlayerA', (0, 1), (0, 3), 2)
        game.move_piece('PlayerB', (5, 1), (5, 3), 2)
        game.move_piece('PlayerA', (5, 2), (5, 3), 1)
        game.move_piece('PlayerB', (0, 2), (0, 3), 1)
        game.move_piece('PlayerA', (4, 5), (5, 5), 1)
        game.move_piece('PlayerB', (1, 5), (0, 5), 1)
        game.move_piece('PlayerA', (5, 5), (5, 3), 2)
        game.move_piece('PlayerB', (0, 5), (0, 3), 2)
        result = game.reserved_move('PlayerA', (0, 3))
        self.assertEqual(result, "successfully moved")

    def test_22(self):
        """ Test to see if a reserved move removed 1 from the player's reserved collection."""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        game.move_piece('PlayerA', (0, 1), (0, 3), 2)
        game.move_piece('PlayerB', (5, 1), (5, 3), 2)
        game.move_piece('PlayerA', (5, 2), (5, 3), 1)
        game.move_piece('PlayerB', (0, 2), (0, 3), 1)
        game.move_piece('PlayerA', (4, 5), (5, 5), 1)
        game.move_piece('PlayerB', (1, 5), (0, 5), 1)
        game.move_piece('PlayerA', (5, 5), (5, 3), 2)
        game.move_piece('PlayerB', (0, 5), (0, 3), 2)
        game.reserved_move('PlayerA', (0, 0))
        result = game.show_reserve('PlayerA')
        self.assertEqual(result, 0)

    def test_23(self):
        """ Test to see if reserved move not in the board will return False."""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        game.move_piece('PlayerA', (0, 1), (0, 3), 2)
        game.move_piece('PlayerB', (5, 1), (5, 3), 2)
        game.move_piece('PlayerA', (5, 2), (5, 3), 1)
        game.move_piece('PlayerB', (0, 2), (0, 3), 1)
        game.move_piece('PlayerA', (4, 5), (5, 5), 1)
        game.move_piece('PlayerB', (1, 5), (0, 5), 1)
        game.move_piece('PlayerA', (5, 5), (5, 3), 2)
        game.move_piece('PlayerB', (0, 5), (0, 3), 2)
        result = game.reserved_move('PlayerA', (0, 7))
        self.assertFalse(result)

    def test_24(self):
        """ Test to see if reserved move out of turn will return False."""
        game = FocusGame(('PlayerA', 'R'), ('PlayerB', 'G'))
        game.move_piece('PlayerA', (0, 0), (0, 1), 1)
        game.move_piece('PlayerB', (5, 0), (5, 1), 1)
        game.move_piece('PlayerA', (0, 1), (0, 3), 2)
        game.move_piece('PlayerB', (5, 1), (5, 3), 2)
        game.move_piece('PlayerA', (5, 2), (5, 3), 1)
        game.move_piece('PlayerB', (0, 2), (0, 3), 1)
        game.move_piece('PlayerA', (4, 5), (5, 5), 1)
        game.move_piece('PlayerB', (1, 5), (0, 5), 1)
        game.move_piece('PlayerA', (5, 5), (5, 3), 2)
        game.move_piece('PlayerB', (0, 5), (0, 3), 2)
        result = game.reserved_move('PlayerB', (0, 0))
        self.assertFalse(result)






if __name__ == '__main__':
    unittest.main(exit=False)
