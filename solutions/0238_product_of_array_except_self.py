from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums); p = 1
        for i, x in enumerate(nums):
            ans[i] = p; p *= x
        p = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= p; p *= nums[i]
        return ans
