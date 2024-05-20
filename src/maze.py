from window import Window
from cell import Cell
from typing import List
import time, random

class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = None
        self.seed = None
        if self.seed:
            random.seed(self.seed)

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def draw_cell(self, i: int, j: int) -> None:
        self.cells[i][j].draw("black")
        self.animate()

    def create_cells(self) -> List[List[Cell]]:
        self.cells = []
        pointer_x = self.x1
        for i in range(self.num_cols):
            pointer_y = self.y1
            new_col = []
            self.cells.append(new_col)
            for j in range(self.num_rows):
                new_col.append(Cell(pointer_x, pointer_x + self.cell_size_x,
                                         pointer_y, pointer_y + self.cell_size_y,
                                         self.win))
                self.draw_cell(i, j)
                pointer_y += self.cell_size_y
            pointer_x += self.cell_size_x
        return self.cells 

    def break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self.cells[self.num_cols - 1][self.num_rows - 1].has_right_wall = False
        self.draw_cell(0, 0)
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)      

    def reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False

    def break_walls_r(self, i: int, j: int):
        self.cells[i][j].visited = True
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbors = []
        for (dir_x, dir_y) in dir:
            adj_x = i + dir_x
            adj_y = j + dir_y
            if (adj_x < 0 or adj_x >= self.num_cols 
                or adj_y < 0 or adj_y >= self.num_rows 
                or self.cells[adj_x][adj_y].visited is True):
                neighbors.append(None)
            else:
                
        choosen_dir = neighbors[random.randrange(0, len(neighbors))]
        if choosen_dir == dir[0]:
            self.cells[i][j].has_right_wall = False
            self.cells[choosen_dir[0]][choosen_dir[1]].has_left_wall = False
            
        elif choosen_dir == dir[1]:
            self.cells[i][j].has_left_wall = False
            self.cells[choosen_dir[0]][choosen_dir[1]].has_right_wall = False
        elif choosen_dir == dir[2]:
            self.cells[i][j].has_bottom_wall = False
            self.cells[choosen_dir[0]][choosen_dir[1]].has_top_wall = False
        elif choosen_dir == dir[3]:
            self.cells[i][j].has_top_wall = False
            self.cells[choosen_dir[0]][choosen_dir[1]].has_bottom_wall = False
        self.draw_cell(i, j)
        self.draw_cell(choosen_dir[0], choosen_dir[1])
        self.break_walls_r(choosen_dir[0], choosen_dir[1])




        


