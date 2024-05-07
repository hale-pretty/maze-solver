from window import Window
from cell import Cell

win = Window(800, 600)
win.wait_for_close()

cell1 = Cell(10, 100, 10, 100, win)
cell2 = Cell(300, 500, 550, 189, win)

cell1.draw("black")
cell2.draw("red")