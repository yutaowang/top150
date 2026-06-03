from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None; count = 0
        for x in nums:
            if count == 0: cand = x
            count += 1 if x == cand else -1
        return cand
