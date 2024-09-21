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
        # print(f"Breaking {self._pos}: Wall {wall}")
        self._walls[wall] = False

    def draw(self, fill_color="black") -> None:
        for i in range(4):
            start, end = self._corners[i % 4], self._corners[(i + 1) % 4]
            line = Line(start, end)

            if self._walls[i]:
                print(f"Cell: Printing: {self._pos}: Wall: {i} Color: {fill_color}")
                self._win.draw_line(line, fill_color)
            else:
                print(f"Cell: Erasing: {self._pos}: Wall: {i}")
                self._win.draw_line(line, "white")

    def _get_walls(self) -> int:
        """_summary_
        Returns the number of walls in the cell
        """
        return sum(self._walls)
