from typing import List
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g=defaultdict(list); indeg=[0]*numCourses
        for a,b in prerequisites: g[b].append(a); indeg[a]+=1
        q=deque([i for i,d in enumerate(indeg) if d==0]); order=[]
        while q:
            x=q.popleft(); order.append(x)
            for y in g[x]:
                indeg[y]-=1
                if indeg[y]==0: q.append(y)
        return order if len(order)==numCourses else []
