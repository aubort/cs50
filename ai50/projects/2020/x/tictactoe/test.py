import unittest

import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

class TestTicTacToe(unittest.TestCase):
    def test_player(self):
        """
        Test player turn
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


    def test_actions(self):
        """
        Test player turn
        """
        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]

        actions = {(0,0), (0,1), (0,2), 
                    (1,0), (1,1), (1,2),
                    (2,0), (2,1), (2,2)}
        
        self.assertEqual(ttt.actions(board), actions)

        board = [[X, EMPTY, O],
                [EMPTY, EMPTY, O],
                [EMPTY, X, EMPTY]]

        actions = {(0,1), 
                    (1,0), (1,1),
                    (2,0), (2,2)}
        
        self.assertEqual(ttt.actions(board), actions)

        board = [[X, X, O],
                [X, O, O],
                [O, X, O]]

        actions = set()
        
        self.assertEqual(ttt.actions(board), actions)

if __name__ == '__main__':
    unittest.main()