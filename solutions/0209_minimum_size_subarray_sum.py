from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=s=0; ans=float('inf')
        for r,x in enumerate(nums):
            s+=x
            while s>=target:
                ans=min(ans,r-l+1); s-=nums[l]; l+=1
        return 0 if ans==float('inf') else ans
