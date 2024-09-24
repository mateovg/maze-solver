from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

WIN_WIDTH = 800
WIN_HEIGHT = 600
CELL_SIZE = 50

def main() -> None:
    win = Window(WIN_WIDTH, WIN_HEIGHT)
    
    num_rows = 50
    num_cols = 50
    margin = 5
    cell_width = (WIN_WIDTH - 2 * margin) / num_cols
    cell_height = (WIN_HEIGHT - 2 * margin) / num_rows

    maze = Maze(margin, num_rows, num_cols, cell_width, cell_height, window=win)
                 
    win.wait_for_close()

if __name__ == "__main__":
    main()