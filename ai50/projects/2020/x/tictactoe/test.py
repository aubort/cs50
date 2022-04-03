import unittest

import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

class TestTicTacToe(unittest.TestCase):
    def test_player(self):
        """
        Test that it can sum a list of integers
        """
        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]

        self.assertEqual(ttt.player(board), X)

        board = [[X, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]

        
        self.assertEqual(ttt.player(board), O)

        board = [[X, EMPTY, EMPTY],
                [EMPTY, O, EMPTY],
                [EMPTY, EMPTY, EMPTY]]

        
        self.assertEqual(ttt.player(board), X)

        board = [[X, X, O],
                [X, O, O],
                [O, X, O]]

        
        self.assertEqual(ttt.player(board), None)


if __name__ == '__main__':
    unittest.main()