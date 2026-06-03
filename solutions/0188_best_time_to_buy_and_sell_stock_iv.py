from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k>=len(prices)//2: return sum(max(0,prices[i]-prices[i-1]) for i in range(1,len(prices)))
        buy=[float('-inf')]*(k+1); sell=[0]*(k+1)
        for p in prices:
            for t in range(1,k+1): buy[t]=max(buy[t],sell[t-1]-p); sell[t]=max(sell[t],buy[t]+p)
        return sell[k]
