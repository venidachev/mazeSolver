from window import Window
from geometry import Line, Point
from maze import Cell

def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.has_top_wall = True
    cell.has_bottom_wall = False
    cell.has_left_wall = True
    cell.has_right_wall = True
    cell.draw(300, 300, 400, 400)
    win.wait_for_close()

if __name__ == "__main__":
    main()