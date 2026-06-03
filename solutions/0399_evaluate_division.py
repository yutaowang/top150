from typing import List
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g=defaultdict(list)
        for (a,b),v in zip(equations,values): g[a].append((b,v)); g[b].append((a,1/v))
        def bfs(s,t):
            if s not in g or t not in g: return -1.0
            q=deque([(s,1.0)]); seen={s}
            while q:
                x,val=q.popleft()
                if x==t: return val
                for y,w in g[x]:
                    if y not in seen: seen.add(y); q.append((y,val*w))
            return -1.0
        return [bfs(a,b) for a,b in queries]
