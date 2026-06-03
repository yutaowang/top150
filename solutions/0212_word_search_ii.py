from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for w in words:
            node=trie
            for c in w: node=node.setdefault(c,{})
            node['$']=w
        m,n=len(board),len(board[0]); res=[]
        def dfs(r,c,node):
            ch=board[r][c]
            if ch not in node: return
            nxt=node[ch]; w=nxt.pop('$',None)
            if w: res.append(w)
            board[r][c]='#'
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and board[nr][nc]!='#': dfs(nr,nc,nxt)
            board[r][c]=ch
        for r in range(m):
            for c in range(n): dfs(r,c,trie)
        return res
