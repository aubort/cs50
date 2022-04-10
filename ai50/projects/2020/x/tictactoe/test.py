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

    def test_winner(self):

        board = [[X, X, X],
                [O, O, EMPTY],
                [O, EMPTY, EMPTY]]
        self.assertEqual(ttt.winner(board), X)

        board = [[X, O, X],
                [O, O, X],
                [X, O, EMPTY]]
        self.assertEqual(ttt.winner(board), O)

        board = [[X, O, X],
                [O, X, X],
                [X, O, O]]
        self.assertEqual(ttt.winner(board), X)

        board = [[X, O, X],
                [O, EMPTY, X],
                [O, EMPTY, X]]
        self.assertEqual(ttt.winner(board), X)

        board = [[X, O, X],
                [O, X, X],
                [O, X, O]]
        self.assertEqual(ttt.winner(board), None)


    def test_terminal(self):
        board = [[X, X, X],
                [O, O, EMPTY],
                [O, EMPTY, EMPTY]]
        self.assertEqual(ttt.terminal(board), True)

        board = [[X, O, X],
                [O, O, X],
                [X, O, EMPTY]]
        self.assertEqual(ttt.terminal(board), True)

        board = [[X, O, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.terminal(board), False)

        board = [[X, O, X],
                [O, X, X],
                [O, X, O]]
        self.assertEqual(ttt.terminal(board), True)

    def test_utility(self):

        board = [[X, O, X],
                [O, X, X],
                [O, X, O]]
        self.assertEqual(ttt.utility(board), 0)

        board = [[X, O, X],
                [O, O, X],
                [X, O, EMPTY]]
        self.assertEqual(ttt.utility(board), -1)

        board = [[X, O, X],
                [O, EMPTY, X],
                [O, EMPTY, X]]
        self.assertEqual(ttt.utility(board), 1)

    def test_get_cell_value(self):

        board = [['A', 'B', 'C'],
                ['D', 'E', 'F'],
                ['G', 'H', 'I']]

        self.assertEqual(ttt.get_cell_value(board, (1, 1)), 'E')
        self.assertEqual(ttt.get_cell_value(board, (0, 2)), 'C')

    def test_minimax(self):

        board = [[EMPTY, X, O],
                [O, X, EMPTY],
                [X, EMPTY, O]]
        ttt.minimax(board)

    # def test_print_board(self):

    #     board = [[EMPTY, X, O],
    #             [O, X, X],
    #             [X, EMPTY, O]]
    #     ttt.print_board(board)

if __name__ == '__main__':
    unittest.main()