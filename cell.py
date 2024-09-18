from graphics import Window, Line, Point
from typing import TypeVar

Cell = TypeVar("Cell", bound="Cell")

class Cell:
    """
    Class to represent a Cell of the maze. 
    """
    def __init__(
        self,
        pos: Point,
        width: int,
        height: int,
        win: Window,
        has_top_wall=True,
        has_right_wall=True,
        has_bottom_wall=True,
        has_left_wall=True,
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
        return Point(self._pos.x + half , self._pos.y + half)

    def draw_path(self, other: Cell, undo=False) -> None:
        fill_color = "gray" if undo else "red"
        center_self = self.get_center()
        center_other = other.get_center()
        line = Line(center_self, center_other)
        self._win.draw_line(line, fill_color)

    def draw(self, fill_color="black") -> None:
        for i in range(4):
            start, end = self._corners[i % 4], self._corners[(i + 1) % 4]
            line = Line(start, end)
            wall = self._walls[i]
            if wall:
                self._win.draw_line(line, fill_color)