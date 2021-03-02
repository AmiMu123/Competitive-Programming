from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        row, col = len(grid), len(grid[0])
        queue = deque()
        dist = -1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))

        while queue:
            row, col, dist = queue.popleft()
            for neighbour in neighbours:
                new_row = neighbour[0] + row
                new_col = neighbour[1] + col
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) \
                        and grid[new_row][new_col] == 0:
                    grid[new_row][new_col] = 1
                    queue.append((new_row, new_col, dist + 1))

        if dist == 0:
            return -1
        return dist
