from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # upper bottom
        row, col = len(board)-1, len(board[0])-1
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.checkborder(board, 0, i, neighbours)
            if board[row][i] == 'O':
                self.checkborder(board, row, i, neighbours)
        # left right
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.checkborder(board, i, 0, neighbours)
            if board[i][col] == 'O':
                self.checkborder(board, i, col, neighbours)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '1':
                    board[i][j] = 'O'

    def checkborder(self, board, i, j, neighbours):
        board[i][j] = '1'
        for neighbour in neighbours:
            new_r = neighbour[0] + i
            new_c = neighbour[1] + j
            if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and board[new_r][new_c] == 'O':
                self.checkborder(board, new_r, new_c, neighbours)
