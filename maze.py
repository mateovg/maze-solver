from graphics import Window, Point

class Maze:
    def __init__(
            self,
            pos: Point,
            num_rows: int,
            num_cols: int,
            cell_size: int,
            window: Window
        ) -> None:
        self._pos = pos
        self.num_rows = num_rows
        