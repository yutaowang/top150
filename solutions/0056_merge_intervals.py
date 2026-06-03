from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(); res=[]
        for a,b in intervals:
            if not res or a>res[-1][1]: res.append([a,b])
            else: res[-1][1]=max(res[-1][1],b)
        return res
