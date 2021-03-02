from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1),
                      (-1, -1), (-1, 1), (1, 1), (1, -1)]
        queue = deque([(0, 0, 1)])
        row, col = len(grid), len(grid)
        if grid[0][0] != 0 or grid[len(grid)-1][len(grid)-1] != 0:
            return -1
        while queue:
            row, col, dist = queue.popleft()
            for neighbour in neighbours:
                new_row = neighbour[0] + row
                new_col = neighbour[1] + col
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid) \
                        and grid[new_row][new_col] == 0:
                    grid[new_row][new_col] = 1
                    queue.append((new_row, new_col, dist + 1))
            if (row, col) == ((len(grid)-1, len(grid)-1)):
                return dist

        return -1
