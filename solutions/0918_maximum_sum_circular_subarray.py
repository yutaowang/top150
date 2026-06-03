from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=sum(nums); max_cur=max_best=min_cur=min_best=nums[0]
        for x in nums[1:]:
            max_cur=max(x,max_cur+x); max_best=max(max_best,max_cur)
            min_cur=min(x,min_cur+x); min_best=min(min_best,min_cur)
        return max_best if max_best<0 else max(max_best,total-min_best)
