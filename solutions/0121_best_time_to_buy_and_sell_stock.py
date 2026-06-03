from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf'); ans = 0
        for p in prices:
            low = min(low, p); ans = max(ans, p-low)
        return ans
