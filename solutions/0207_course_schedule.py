from typing import List
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=defaultdict(list); indeg=[0]*numCourses
        for a,b in prerequisites: g[b].append(a); indeg[a]+=1
        q=deque([i for i,d in enumerate(indeg) if d==0]); seen=0
        while q:
            x=q.popleft(); seen+=1
            for y in g[x]:
                indeg[y]-=1
                if indeg[y]==0: q.append(y)
        return seen==numCourses
