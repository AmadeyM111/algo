class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def some_graph_algorithm(grid):
        nei_dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
        nei_dirs = (Cell(elem[0], elem[1]) for elem in nei_dirs)

        current = ...
        for direction in nei_dirs:
            nei = Cell(current.row + direction.row, current.col + direction.col)
            if nei.row < 0 or nei.row == len(grid) \
            or nei.col < 0 or nei.col == len(grid[0]):
                continue
            if grid[nei.row][nei.col] != '#':
                ...

