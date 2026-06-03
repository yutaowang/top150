from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def back(s,l,r):
            if len(s)==2*n: res.append(s); return
            if l<n: back(s+'(',l+1,r)
            if r<l: back(s+')',l,r+1)
        back('',0,0); return res
