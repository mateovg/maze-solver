from graphics import Window, Line, Point
from cell import Cell

WIN_WIDTH = 800
WIN_HEIGHT = 600
CELL_SIZE = 50

def main() -> None:
    win = Window(WIN_WIDTH, WIN_HEIGHT)
    
    lineA = Line(Point(0, 0), Point(800, 600))
    lineB = Line(Point(800, 0), Point(0, 600))
 
    prev_cell = None
    for x in range(0, 800, 50):
        for y in range(0, 600, 50):
            curr_cell = Cell(True, True, True, True, Point(x, y), 50, win)
            curr_cell.draw()
            if prev_cell:
                curr_cell.draw_path(prev_cell)
            prev_cell = curr_cell
                 
    win.wait_for_close()

if __name__ == "__main__":
    main()