from queue import deque


class Solution:
    def orangesRotting(self, grid):
        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque()
        minute_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            row, col, minute_count = queue.popleft()
            for neighbour in neighbours:
                new_row = row + neighbour[0]
                new_col = col + neighbour[1]
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) \
                        and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col, minute_count + 1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minute_count
