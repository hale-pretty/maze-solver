from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.rootWidget = Tk()
        self.rootWidget.title = "Duy xau xi"
        self.canvasWidget = Canvas(self.rootWidget, width=self.width, height=self.height)
        self.canvasWidget.pack()
        self.isRunning = False
        self.rootWidget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.rootWidget.update_idletasks()
        self.rootWidget.update()
        
    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning is True:
            self.redraw()

    def close(self):
        self.isRunning = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvasWidget, fill_color)
        

        