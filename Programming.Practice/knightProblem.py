import unittest
from typing import List, Set

class KT():
    '''A chess-knight's touch begins at (0,0), has to visit each chess
    position exactly once. If every board position is reached, then
    the knight could complete its quest'''
    #Number of rows/columns on a chess-board
    N:int = 8
    sol:List
    #A set of
    move_set:Set = {(2, 1), (1, 2),
                 (-1, 2), (-2, 1),
                 (-2, -1), (-1, -2),
                 (1, -2), (2, -1)}
    def __init__(self):
        '''Initialize the problem statement.'''
        pass
    @staticmethod
    def _move_is_safe_(start_x, start_y, x_, y_):
        return (
                (start_x+x_ >= 0) and
                (start_x +x_ < KT.N) and
                start_y + y_ >= 0 and
                start_y + y_ < KT.N and
                KT.sol[start_x+x_][start_y+y_] == -1
        )
    def solveKT(self):
        '''A driver method to call recursive backtracking solution'''
        KT.sol = [[-1 for i in range(KT.N)] for j in range(KT.N)]
        KT.sol[0][0] = 0
        print("BEFORE: Solution:", KT.sol[1][0])
        if False == self.solve_KT_recursive(0, 0, 1):
            print("Solution Not Found", KT.sol)
            return False
        else:
            print("AFTER Solution:", KT.sol)
            return True
    @staticmethod
    def solve_KT_recursive(start_x:int, start_y:int, move:int):
        '''move will go to sit sol matrix if it's a viable solution'''
        if move == (KT.N)*(KT.N):
            return True
        #Move Knight present at (start_x, start_y) to next unexplored move position
        for (x_, y_) in KT.move_set:
            if KT._move_is_safe_(start_x, start_y, x_, y_):
                KT.sol[start_x+x_][start_y+y_] = move
                if True == KT.solve_KT_recursive(start_x + x_, start_y + y_, move + 1):
                    return True
                else:
                    KT.sol[start_x+x_][start_y+y_] = -1
        return False

class MyTestCase(unittest.TestCase):
    def test_knights_tour(self):
        kt_problem = KT()
        assert True == kt_problem.solveKT()


if __name__ == '__main__':
    unittest.main()
