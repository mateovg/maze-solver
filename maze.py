from time import sleep
import random
from typing import List
from cell import Cell
from graphics import Window, Point

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

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
        self._break_walls_r(0, 0)

    def _create_cells(self) -> None:
        for row in range(self._num_rows):
            y = self._pos.y + self._cell_height * row
            for col in range(self._num_cols):
                x = self._pos.x + self._cell_width * col
                self._cell_grid[row][col] = Cell(
                        Point(x, y), self._cell_width, self._cell_height, self._win
                    )
        self._draw_cells_all(to_sleep=False)
                
    def _break_cell_wall(self, row: int, col: int, wall: int | None = None) -> None:
        self._cell_grid[row][col].break_wall(wall=wall)
        self._draw_cell(row, col)
    
    def _get_neighbors(self, row: int, col: int) -> List[tuple[int, int]]:
        neighbors = []
        for wall, (dr, dc) in enumerate(DIRECTIONS):
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < self._num_rows) and (0 <= new_col < self._num_cols):
                neighbors.append([new_row, new_col, wall])
                    
        return neighbors           
         
    def _break_walls_r(self, row: int, col: int) -> None:
        print(f"Call on {row}, {col}")
        neighbors = self._get_neighbors(row, col)
        # print(f"{neighbors=}")
        options = [(r, c, w) for (r, c, w) in neighbors if not self._cell_visited[r][c]]
        # print(f"{options=}")
        self._cell_visited[row][col] = True        

        if len(options) == 0:
            self._draw_cell(row, col, color = "gray")
            return

        new_row, new_col, wall = random.choice(options)
       
        self._break_cell_wall(row, col, wall=wall) 
        self._break_cell_wall(new_row, new_col, wall=(wall + 2) % 4)
        
        self._draw_cell(row, col, color="red")
        self._break_walls_r(new_row, new_col)
   
    
    def _break_entrance_and_exit(self) -> None:
        self._break_cell_wall(0, 0, 0)
        self._break_cell_wall(self._num_rows - 1, self._num_cols - 1, 2)
         
    def _draw_cell(self, row: int, col: int, to_sleep: bool = True, color: str = "black") -> None:
        print(f"Drawing cell: {row},{col}")
        if self._win is None:
            return
        cell = self._cell_grid[row][col]
        print(f"{cell._walls}")
        cell.draw(fill_color=color)
        self._animate(to_sleep=to_sleep)
        
    def _draw_cells_all(self, to_sleep: bool) -> None:
         for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._draw_cell(row, col, to_sleep=to_sleep)       
    
    def _animate(self, to_sleep: bool) -> None:
        if self._win is None:
            return
        self._win.redraw()
        if to_sleep:
            print("Sleeping...")
            sleep(0.025)