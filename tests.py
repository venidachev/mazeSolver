import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze.cells),
            num_cols,
        )
        self.assertEqual(
            len(maze.cells[0]),
            num_rows,
        )
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze.cells),
            num_cols,
        )
        self.assertEqual(
            len(maze.cells),
            num_cols,
        )

if __name__ == "__main__":
    unittest.main()