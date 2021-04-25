#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
from collections import deque


def minimumMoves(grid, startX, startY, goalX, goalY):
    # row,col = len(grid),len(grid)
    queue = deque([(startX, startY, 0)])
    visited = set([(startX, startY)])
    while queue:
        row, col, dist = queue.popleft()
        # visited.add((row,col))
        if (row, col) == (goalX, goalY):
            return dist
        for i in range(row-1, -1, -1):
            new_row = i
            new_col = col
            if grid[new_row][new_col] == 'X':
                break
            if (new_row, new_col) not in visited:
                queue.append((new_row, new_col, dist + 1))
                visited.add((new_row, new_col))
        for i in range(row + 1, len(grid)):
            new_row = i
            new_col = col
            if grid[new_row][new_col] == 'X':
                break
            if (new_row, new_col) not in visited:
                queue.append((new_row, new_col, dist + 1))
                visited.add((new_row, new_col))
        for i in range(col + 1, len(grid)):
            new_row = row
            new_col = i
            if grid[new_row][new_col] == 'X':
                break
            if (new_row, new_col) not in visited:
                queue.append((new_row, new_col, dist + 1))
                visited.add((new_row, new_col))
        for i in range(col - 1, -1, -1):
            new_row = row
            new_col = i
            if grid[new_row][new_col] == 'X':
                break
            if (new_row, new_col) not in visited:
                queue.append((new_row, new_col, dist + 1))
                visited.add((new_row, new_col))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
