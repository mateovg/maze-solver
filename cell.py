import random
from graphics import Window, Line, Point
from typing import TypeVar

Cell = TypeVar("Cell", bound="Cell")


class Cell:
    """
    Class to represent a Cell of the maze.
    """

    def __init__(
        self,
        pos: Point = Point(0, 0),
        width: int = 50,
        height: int = 50,
        win: Window = None,
        has_top_wall: bool = True,
        has_right_wall: bool = True,
        has_bottom_wall: bool = True,
        has_left_wall: bool = True,
    ) -> None:
        self._walls = [has_top_wall, has_right_wall, has_bottom_wall, has_left_wall]
        self._pos = pos
        self._width = width
        self._height = height
        self._win = win
        self._corners = [
            Point(self._pos.x, self._pos.y),
            Point(self._pos.x + self._width, self._pos.y),
            Point(self._pos.x + self._width, self._pos.y + self._height),
            Point(self._pos.x, self._pos.y + self._height),
        ]

    def get_center(self) -> Point:
        half = self._size // 2
        return Point(self._pos.x + half, self._pos.y + half)

    def draw_path(self, other: Cell, undo: bool = False) -> None:
        if self._win is None:
            return

        fill_color = "gray" if undo else "red"
        center_self = self.get_center()
        center_other = other.get_center()
        line = Line(center_self, center_other)

        self._win.draw_line(line, fill_color)

    def break_wall(self, wall: int | None = None):
        """Breaks the wall of the Cell by setting it false

        Args:
            wall (int | None, optional): Wall to break. o => Up, 1 => right, 2 => down, 3 => left. Defaults to random.
        """
        if wall is None:
            wall = random.randint(0, 3)
        print(f"Breaking {self._pos}: Wall {wall}")
        self._walls[wall] = False

    def draw(self, fill_color="black") -> None:
        # print(f"Drawing cell... Walls: {self._walls}")
        for wall, to_draw in enumerate(self._walls):
            if to_draw:
                self._draw_wall(wall, fill_color)
            else:
                self._erase_wall(wall) 

            
    def _draw_wall(self, wall: int, fill_color: str) -> None:
        start, end = self._corners[wall % 4], self._corners[(wall + 1) % 4]
        line = Line(start, end)
        self._win.draw_line(line, fill_color)
    
    def _erase_wall(self, wall: int) -> None:
        self._draw_wall(wall, fill_color="white")

    def _get_walls(self) -> int:
        """_summary_
        Returns the number of walls in the cell
        """
        return sum(self._walls)
