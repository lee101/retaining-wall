import unittest

import retaining_wall


class RetainingWallTest(unittest.TestCase):
    def test_retaining_wall(self):
        wall = retaining_wall.RetainingWallSolver().retaining_wall([4, 4, 4], [4, 2, 2, 3, 1])
        self.assertEqual(len(wall['cuts']), 2)

        wall = retaining_wall.RetainingWallSolver().retaining_wall([4, 4, 4], [2, 2, 2, 2])
        self.assertEqual(len(wall['cuts']), 2)

        wall = retaining_wall.RetainingWallSolver().retaining_wall([4, 4, 4, 2], [2, 2, 2, 2, 2])
        self.assertEqual(len(wall['cuts']), 2)


if __name__ == '__main__':
    unittest.main()
