import unittest

import retaining_wall


class RetainingWallTest(unittest.TestCase):
    def test_retaining_wall(self):
        solver = retaining_wall.RetainingWallSolver()
        wall = solver.retaining_wall([4, 4, 4], [4, 2, 2, 3, 1])
        self.assertEqual(len(wall['cuts']), 2)

        wall = solver.retaining_wall([4, 4, 4], [2, 2, 2, 2])
        self.assertEqual(len(wall['cuts']), 2)

        wall = solver.retaining_wall([4, 4, 4, 2], [2, 2, 2, 2, 2])
        self.assertEqual(len(wall['cuts']), 2)

        wall = solver.retaining_wall([4, 4, 4, 2], [2, 2, 2, 2, 2]*10)
        self.assertFalse(wall)

        wall = solver.retaining_wall([4, 4, 4, 2]*10, [2, 2, 2, 2, 2])
        self.assertFalse(len(wall['cuts']), 0)

        wall = solver.retaining_wall(range(100), [2, 2, 2, 2, 2])
        self.assertFalse(len(wall['cuts']), 0)


if __name__ == '__main__':
    unittest.main()
