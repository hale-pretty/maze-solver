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
    
    def draw(self, fill_color: str) -> None:
        top_left_point = Point(self.x1, self.y1)
        bot_left_point = Point(self.x1, self.y2)
        top_right_point = Point(self.x2, self.y1)
        bot_right_point = Point(self.x2, self.y2)
        if self.has_left_wall:
            self.win.draw_line(Line(top_left_point, bot_left_point), fill_color)
        if self.has_right_wall:
            self.win.draw_line(Line(top_right_point, bot_right_point), fill_color)
        if self.has_top_wall:
            self.win.draw_line(Line(top_left_point, top_right_point), fill_color)
        if self.has_bottom_wall:
            self.win.draw_line(Line(bot_left_point, bot_right_point), fill_color)
        