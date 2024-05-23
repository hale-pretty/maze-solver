from window import Window
from maze import Maze

win = Window(1200, 1200)

m1 = Maze(100, 100, 8, 10, 100, 100, win)
m1.create_cells()
m1.break_entrance_and_exit()
m1.break_walls_r(0, 0)
m1.reset_cells_visited()
m1.solve()

win.wait_for_close()
