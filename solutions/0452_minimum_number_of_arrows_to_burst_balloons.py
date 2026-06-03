from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1]); arrows=0; end=None
        for a,b in points:
            if end is None or a>end:
                arrows+=1; end=b
        return arrows
