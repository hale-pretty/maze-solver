from window import Window
from maze import Maze

win = Window(1200, 1200)

m1 = Maze(10, 10, 10, 8, 50, 50, win)
m1.create_cells()
m1.break_entrance_and_exit()
m1.break_walls_r(0, 0)
# m1.reset_cells_visited()


win.wait_for_close()
