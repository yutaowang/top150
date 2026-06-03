from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m,n=len(board),len(board[0])
        dirs=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for r in range(m):
            for c in range(n):
                live=sum(0<=r+dr<m and 0<=c+dc<n and board[r+dr][c+dc]&1 for dr,dc in dirs)
                if board[r][c] and live in (2,3): board[r][c]|=2
                if not board[r][c] and live==3: board[r][c]|=2
        for r in range(m):
            for c in range(n): board[r][c] >>= 1
