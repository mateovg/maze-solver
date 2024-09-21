import unittest

from cell import Cell
from graphics import Point
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, num_rows, num_cols, 10, 10)
        
        self.assertEqual(
            len(maze._cell_grid),
            num_rows,
        )
        self.assertEqual(
            len(maze._cell_grid[0]),
            num_cols,
        )
    
    def test_maze_break_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            maze._cell_grid[0][0]._get_walls(),
            3
        )
        
    def test_cell_break_entrance_exit(self):
        cell = Cell() 
        cell.break_wall(0)
        
        self.assertEqual(
            cell._get_walls(),
            3
        )
        
        
if __name__ == "__main__":
    unittest.main()
    