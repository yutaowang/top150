from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def pos(x):
            r=(x-1)//n; c=(x-1)%n
            if r%2: c=n-1-c
            return n-1-r,c
        q=deque([(1,0)]); seen={1}
        while q:
            x,d=q.popleft()
            if x==n*n: return d
            for y in range(x+1,min(x+6,n*n)+1):
                r,c=pos(y); z=board[r][c] if board[r][c]!=-1 else y
                if z not in seen: seen.add(z); q.append((z,d+1))
        return -1
