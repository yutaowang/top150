from typing import List
from collections import defaultdict
from math import gcd
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2: return len(points)
        ans=0
        for i,(x1,y1) in enumerate(points):
            cnt=defaultdict(int)
            for x2,y2 in points[i+1:]:
                dx,dy=x2-x1,y2-y1; g=gcd(dx,dy); cnt[(dx//g,dy//g)] += 1
            ans=max(ans, 1 + (max(cnt.values()) if cnt else 0))
        return ans
