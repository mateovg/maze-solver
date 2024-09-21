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
            seed: int = None,
            window: Window | None = None,
        ) -> None:
        self._pos = Point(margin, margin)
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_grid: List[List[Cell]] = [[None] * num_cols for _ in range(num_rows)]
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = window
        
        self._cell_visited: List[List[Cell]] = [[False] * num_cols for _ in range(num_rows)]
        self._seed = seed

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:
        for row in range(self._num_rows):
            y = self._pos.y + self._cell_height * row
            for col in range(self._num_cols):
                x = self._pos.x + self._cell_width * col
                self._cell_grid[row][col] = Cell(
                        Point(x, y), self._cell_width, self._cell_height, self._win
                    )
        for row in self._cell_grid:
            for cell in row:
                self._draw_cell(cell)
                
    def _break_entrance_and_exit(self) -> None:
        cells = [self._cell_grid[0][0], self._cell_grid[-1][-1]]
        for cell in cells:
            cell.break_wall()
            self._draw_cell(cell)
                
    def _draw_cell(self, cell: Cell) -> None:
        if self._win is None:
            return
        cell.draw()
        self._animate()
    
    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        # sleep(0.01)