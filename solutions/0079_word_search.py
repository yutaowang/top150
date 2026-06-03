from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        def dfs(r,c,i):
            if i==len(word): return True
            if r<0 or c<0 or r>=m or c>=n or board[r][c]!=word[i]: return False
            ch=board[r][c]; board[r][c]='#'
            ok=dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            board[r][c]=ch; return ok
        return any(dfs(r,c,0) for r in range(m) for c in range(n))
