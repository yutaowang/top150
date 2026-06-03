from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0]); dp=[0]*n; dp[0]=1
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c]: dp[c]=0
                elif c: dp[c]+=dp[c-1]
        return dp[-1]
