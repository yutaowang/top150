from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def back(start,path):
            if len(path)==k: res.append(path[:]); return
            for x in range(start,n+1): back(x+1,path+[x])
        back(1,[]); return res
