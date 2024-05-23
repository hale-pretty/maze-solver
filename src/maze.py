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
        pointer_y = self.y1
        for i in range(self.num_rows):
            pointer_x = self.x1
            new_row = []
            self.cells.append(new_row)
            for j in range(self.num_cols):
                new_row.append(Cell(pointer_x, pointer_x + self.cell_size_x,
                                         pointer_y, pointer_y + self.cell_size_y,
                                         self.win))
                self.draw_cell(i, j)
                pointer_x += self.cell_size_x
            pointer_y += self.cell_size_y
        return self.cells 

    def break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self.cells[self.num_rows - 1][self.num_cols - 1].has_right_wall = False
        self.draw_cell(0, 0)
        self.draw_cell(self.num_rows - 1, self.num_cols - 1)      

    def reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.cells[i][j].visited = False

    def break_walls_r(self, i: int, j: int):
        self.cells[i][j].visited = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for idx, (dir_x, dir_y) in enumerate(directions):
            adj_x = i + dir_x
            adj_y = j + dir_y
            if (adj_x < 0 or adj_x >= self.num_rows 
                or adj_y < 0 or adj_y >= self.num_cols):
                continue
            neighbors.append((adj_x, adj_y, idx))
        while len(neighbors) != 0:
            choosen_dir = neighbors.pop(random.randrange(len(neighbors)))
            if self.cells[choosen_dir[0]][choosen_dir[1]].visited:
                continue
            if choosen_dir[2] == 0:
                self.cells[i][j].has_right_wall = False
                self.cells[choosen_dir[0]][choosen_dir[1]].has_left_wall = False
            elif choosen_dir[2] == 1:
                self.cells[i][j].has_left_wall = False
                self.cells[choosen_dir[0]][choosen_dir[1]].has_right_wall = False
            elif choosen_dir[2] == 2:
                self.cells[i][j].has_bottom_wall = False
                self.cells[choosen_dir[0]][choosen_dir[1]].has_top_wall = False
            elif choosen_dir[2] == 3:
                self.cells[i][j].has_top_wall = False
                self.cells[choosen_dir[0]][choosen_dir[1]].has_bottom_wall = False
            self.break_walls_r(choosen_dir[0], choosen_dir[1])
        self.draw_cell(i, j)

    def solve_r(self, row: int, col: int):
        self.animate()
        self.cells[row][col].visited = True
        if row == self.num_rows - 1 and col == self.num_cols - 1:
            out_x = self.x1 + self.cell_size_x * self.num_cols
            out_y = self.y1 + self.cell_size_y * (self.num_rows - 1)
            self.cells[row][col].draw_move(Cell(out_x, out_x + self.cell_size_x, out_y, out_y + self.cell_size_y, self.win))
            return True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(4):
            (dir_x, dir_y) = directions[i]
            adj_x = row + dir_x
            adj_y = col + dir_y
            if (adj_x < 0 or adj_x >= self.num_rows 
                or adj_y < 0 or adj_y >= self.num_cols):
                continue
            if (self.cells[adj_x][adj_y].visited is False and
                ((i == 0 and self.cells[row][col].has_right_wall is False) or
                (i == 1 and self.cells[row][col].has_left_wall is False) or
                (i == 2 and self.cells[row][col].has_bottom_wall is False) or
                (i == 3 and self.cells[row][col].has_top_wall is False))):
                self.cells[row][col].draw_move(self.cells[adj_x][adj_y])
                if self.solve_r(adj_x, adj_y):
                    return True
                else:
                    self.cells[row][col].draw_move(self.cells[adj_x][adj_y], True)
        return False

    def solve(self):
        Cell(self.x1 - self.cell_size_x, self.x1, self.y1, self.y1 + self.cell_size_y, self.win).draw_move(self.cells[0][0])
        return self.solve_r(0, 0)






        


