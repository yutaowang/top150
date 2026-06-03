from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0]); dp=[0]*(n+1); best=0
        for r in range(1,m+1):
            prev=0
            for c in range(1,n+1):
                tmp=dp[c]
                if matrix[r-1][c-1]=='1': dp[c]=1+min(dp[c],dp[c-1],prev); best=max(best,dp[c])
                else: dp[c]=0
                prev=tmp
        return best*best
