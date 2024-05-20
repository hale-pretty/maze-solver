from window import Window
from line import Line
from point import Point

class Cell:
    def __init__(self, x1: int, x2: int, y1: int, y2: int, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win
        self.visited = False
    
    def draw(self, fill_color: str) -> None:
        top_left_point = Point(self.x1, self.y1)
        bot_left_point = Point(self.x1, self.y2)
        top_right_point = Point(self.x2, self.y1)
        bot_right_point = Point(self.x2, self.y2)
        left_wall = Line(top_left_point, bot_left_point)
        right_wall = Line(top_right_point, bot_right_point)
        top_wall = Line(top_left_point, top_right_point)
        bot_wall = Line(bot_left_point, bot_right_point)
        if self.has_left_wall:
            self.win.draw_line(left_wall, fill_color)
        if not self.has_left_wall:
            self.win.draw_line(left_wall, "#d9d9d9")
        if self.has_right_wall:
            self.win.draw_line(right_wall, fill_color)
        if not self.has_right_wall:
            self.win.draw_line(right_wall, "#d9d9d9")
        if self.has_top_wall:
            self.win.draw_line(top_wall, fill_color)
        if not self.has_top_wall:
            self.win.draw_line(top_wall, "#d9d9d9")
        if self.has_bottom_wall:
            self.win.draw_line(bot_wall, fill_color)
        if not self.has_bottom_wall:
            self.win.draw_line(bot_wall, "#d9d9d9")
    
    def center_point(self) -> Point:
        return Point((self.x1 + self.x2)/2, (self.y1 + self.y2)/2)

    def draw_move(self, to_cell, undo=False) -> None:
        center_point = self.center_point()
        to_center_point = to_cell.center_point()
        move = Line(center_point, to_center_point)
        if undo is False:
            self.win.draw_line(move, "red")
        else:
            self.win.draw_line(move, "gray")

        