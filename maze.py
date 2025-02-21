from window import Window
from geometry import Line, Point


class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win

    def draw(self, x1: int , y1: int, x2: int, y2: int):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line)

    def draw_move(self, to_cell: "Cell", undo=False):
        x1 = (self.x1 + self.x2) // 2
        y1 = (self.y1 + self.y2) // 2
        x2 = (to_cell.x1 + to_cell.x2) // 2
        y2 = (to_cell.y1 + to_cell.y2) // 2
        line = Line(Point(x1, y1), Point(x2, y2))
        if undo:
            self.win.draw_line(line, "red")
        else:
            self.win.draw_line(line, "gray")