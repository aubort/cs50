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
        Test player action
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

    def test_result(self):
        """
        Test result
        """
        board = [[X, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]

        # Illegal move
        self.assertRaises(Exception, ttt.result, board, (0,0))

        # Player X
        board = [[X, O, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]

        board_result = [[X, O, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, X, EMPTY]]
        
        self.assertListEqual(ttt.result(board, (2,1)), board_result)

        # Player O
        board = [[X, O, EMPTY],
                [EMPTY, O, EMPTY],
                [EMPTY, X, EMPTY]]

        board_result = [[X, O, X],
                [EMPTY, O, EMPTY],
                [EMPTY, X, EMPTY]]
        
        self.assertListEqual(ttt.result(board, (0,2)), board_result)

if __name__ == '__main__':
    unittest.main()