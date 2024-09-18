from graphics import Window, Line, Point
from typing import TypeVar

Cell = TypeVar("Cell", bound="Cell")

class Cell:
    def __init__(
        self,
        has_top_wall: bool,
        has_right_wall: bool,
        has_bottom_wall: bool,
        has_left_wall: bool,
        pos: Point,
        size: int,
        win: Window
    ) -> None:
        self._walls = [has_top_wall, has_right_wall, has_bottom_wall, has_left_wall]
        self._pos = pos
        self._size = size
        self._win = win

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
        dx, dy = self._size, 0
        a = self._pos
        b = Point(a.x + dx, a.y + dy)
        line = Line(a, b)

        for wall in self._walls:
            if wall:
                self._win.draw_line(line, fill_color)
            dx, dy = -dy, dx
            a = line.b
            b = Point(a.x + dx, a.y + dy)
            line = Line(a, b)