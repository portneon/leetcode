class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dis = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, 1], [1, 1], [-1, -1], [1, -1]]
        for b in range(m):
            for d in range(n):
                alive = 0

                for e in dis:
                    if 0 <= b + e[0] < m and 0 <= d + e[1] < n:

                        if board[b + e[0]][d + e[1]] == 1 or board[b + e[0]][d + e[1]] == 2:
                            alive += 1
                if alive >= 2 and alive <= 3 and board[b][d] == 1:
                    board[b][d] = 1
                if alive == 3 and board[b][d] == 0:
                    board[b][d] = 3
                if (alive < 2 or alive > 3) and board[b][d] == 1:
                    board[b][d] = 2
        for b in range(m):
            for d in range(n):
                board[b][d] = board[b][d] % 2
