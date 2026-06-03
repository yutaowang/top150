class Solution:
    def totalNQueens(self, n: int) -> int:
        cols=d1=d2=set(); ans=0
        def back(r):
            nonlocal ans
            if r==n: ans+=1; return
            for c in range(n):
                if c in cols or r-c in d1 or r+c in d2: continue
                cols.add(c); d1.add(r-c); d2.add(r+c); back(r+1); cols.remove(c); d1.remove(r-c); d2.remove(r+c)
        back(0); return ans
