class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        max_area = 0
        neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count = [0]
                    self.dfs(grid, i, j, neighbours, count)
                    max_area = max(max_area, count[0])
        return max_area

    def dfs(self, grid, i, j, neighbours, count):
        count[0] += 1
        grid[i][j] = 0
        for neighbour in neighbours:
            new_r = neighbour[0] + i
            new_c = neighbour[1] + j
            if 0 <= new_r < len(grid) and \
                0 <= new_c < len(grid[0]) \
                    and grid[new_r][new_c] == 1:
                self.dfs(grid, new_r, new_c, neighbours, count)
