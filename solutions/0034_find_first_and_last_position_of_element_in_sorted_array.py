from typing import List
import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=bisect.bisect_left(nums,target); r=bisect.bisect_right(nums,target)-1
        return [l,r] if l<=r else [-1,-1]
