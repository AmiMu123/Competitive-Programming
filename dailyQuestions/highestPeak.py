from queue import deque


class Solution:
    def highestPeak(self, isWater):
        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque()
        visited = set()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    queue.append((i, j, 0))
                    isWater[i][j] = 0
                    visited.add((i, j))
        while queue:
            row, col, height = queue.popleft()
            for neighbour in neighbours:
                new_row = row + neighbour[0]
                new_col = col + neighbour[1]
                if 0 <= new_row < len(isWater) and 0 <= new_col < len(isWater[0]) \
                        and (new_row, new_col) not in visited:
                    isWater[new_row][new_col] = height + 1
                    queue.append((new_row, new_col, height + 1))
                    visited.add((new_row, new_col))
        return isWater
