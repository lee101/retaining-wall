import unittest

import retaining_wall


class RetainingWallTest(unittest.TestCase):
    def test_retaining_wall(self):
        solver = retaining_wall.RetainingWallSolver()
        wall = solver.retaining_wall([6], [4, 2])
        self.assertEqual(len(wall['cuts']), 1)
        self.assertEqual(wall['cuts'][0]['wood_num'], 0)
        self.assertEqual(wall['cuts'][0]['cut_amount'], 2)

        wall = solver.retaining_wall([6, 4], [2, 2])
        self.assertEqual(len(wall['cuts']), 1)

        wall = solver.retaining_wall([6, 4, 2], [2, 2, 2])
        self.assertEqual(len(wall['cuts']), 1)
        self.assertEqual(wall['cuts'][0]['wood_num'], 1)
        self.assertEqual(wall['cuts'][0]['cut_amount'], 2)

        wall = solver.retaining_wall([4, 4, 4], [4, 2, 2, 3, 1])
        self.assertEqual(len(wall['cuts']), 2)

        wall = solver.retaining_wall([4, 4, 4], [2, 2, 2, 2])
        self.assertEqual(len(wall['cuts']), 2)

        wall = solver.retaining_wall([4, 4, 4, 2], [2, 2, 2, 2, 2])
        self.assertEqual(len(wall['cuts']), 2)

        wall = solver.retaining_wall([4, 4, 4, 2], [2, 2, 2, 2, 2] * 10)
        self.assertFalse(wall)

        wall = solver.retaining_wall([4, 4, 4, 2] * 10, [2, 2, 2, 2, 2])
        self.assertFalse(len(wall['cuts']), 0)

        wall = solver.retaining_wall([4, 4, 4, 2] * 10, [2, 2, 2, 2, 2])
        self.assertFalse(len(wall['cuts']), 0)



        wall = solver.retaining_wall(list(range(20)), [2, 2, 2, 2, 2])
        self.assertEqual(len(wall['cuts']), 3)


        wall = solver.retaining_wall(list(range(100)), list(range(100, 200)))
        self.assertFalse(wall)

        wall = solver.retaining_wall(list(range(100, 105)), list(range(100)))
        self.assertFalse(wall)


if __name__ == '__main__':
    unittest.main()
