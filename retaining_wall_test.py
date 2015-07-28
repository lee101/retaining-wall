import unittest

import retaining_wall


class RetainingWallTest(unittest.TestCase):
    def test_retaining_wall(self):
        wall = retaining_wall.RetainingWallSolver().retaining_wall([4, 4, 4], [
            [2, 2, 2, 2, 2],
        ])
        self.assertEqual(len(wall['cuts']), 1)

        wall = retaining_wall.RetainingWallSolver().retaining_wall([4, 4, 4], [[
            2, 2, 2, 2],
        ])
        self.assertEqual(len(wall['cuts']), 0)

        wall = retaining_wall.RetainingWallSolver().retaining_wall([4, 4, 4, 2], [
            [2, 2, 2, 2, 2],
        ])
        self.assertEqual(len(wall['cuts']), 0)

        wall = retaining_wall.RetainingWallSolver().retaining_wall([4, 4, 4], [
            [2, 2, 2],
            [2, 2, 2],
        ])
        self.assertEqual(len(wall['cuts']), 1)

        wall = retaining_wall.RetainingWallSolver().retaining_wall([15], [
            [2, 2, 2],
            [2, 2, 2],
        ])
        self.assertEqual(len(wall['cuts']), 2)

        wall = retaining_wall.RetainingWallSolver().retaining_wall([12], [
            [2, 2, 2],
            [2, 2, 2],
        ])
        self.assertEqual(len(wall['cuts']), 1)

        # wall = retaining_wall.RetainingWallSolver().retaining_wall([4, 4, 4, 2, 2, 3, 4, 5, 6, 2, 4, 5, 3],
        #                                                            [2, 2, 2, 2, 2, 2, 2, 2, 2])
        # self.assertEqual(len(wall['cuts']), 2)


if __name__ == '__main__':
    unittest.main()
