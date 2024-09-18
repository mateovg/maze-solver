from tkinter import Tk, BOTH, Canvas
from typing import TypeVar, Tuple



class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def coords(self) -> tuple[int, int]:
        return (self.x, self.y)


class Line:
    def __init__(self, a: Point, b: Point) -> None:
        self.a = a
        self.b = b

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        x1, y1 = self.a.coords()
        x2, y2 = self.b.coords()

        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)





class Window:

    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver 9002")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Widow closing...")

    def draw_line(self, line: Line, fill_color="black") -> None:
        line.draw(self.__canvas, fill_color)

    def close(self) -> None:
        self.__is_running = False
