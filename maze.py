from time import sleep
from typing import List
from cell import Cell
from graphics import Window, Point

class Maze:
    def __init__(
            self,
            margin: int,
            num_rows: int,
            num_cols: int,
            cell_width: int,
            cell_height: int,
            window: Window
        ) -> None:
        self._pos = Point(margin, margin)
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_grid: List[List[Cell]] = [[None] * num_cols for _ in range(num_rows)]
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = window
        
        self._create_cells()
        
    def _create_cells(self) -> None:
        for row in range(self._num_rows):
            y = self._pos.y + self._cell_height * row
            for col in range(self._num_cols):
                x = self._pos.x + self._cell_width * col
                self._cell_grid[row][col] = Cell(
                    Point(x, y), self._cell_width, self._cell_height, self._win
                    )

                self._draw_cell(row, col)
                
    def _draw_cell(self, row: int, col: int) -> None:
        if self._win is None:
            return
        self._cell_grid[row][col].draw()
        self._animate
    
    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.5)