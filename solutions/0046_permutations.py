from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back(path,rem):
            if not rem: res.append(path); return
            for i,x in enumerate(rem): back(path+[x], rem[:i]+rem[i+1:])
        back([],nums); return res
