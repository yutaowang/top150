from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(); res=[]
        def back(start,rem,path):
            if rem==0: res.append(path[:]); return
            for i in range(start,len(candidates)):
                if candidates[i]>rem: break
                back(i, rem-candidates[i], path+[candidates[i]])
        back(0,target,[]); return res
