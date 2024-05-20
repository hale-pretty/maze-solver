import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(150, 150)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        m1.create_cells()
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()
