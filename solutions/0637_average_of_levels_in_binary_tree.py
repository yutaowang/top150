from typing import List
from collections import deque
class Solution:
    def averageOfLevels(self, root) -> List[float]:
        q=deque([root]); res=[]
        while q:
            vals=[]
            for _ in range(len(q)):
                n=q.popleft(); vals.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            res.append(sum(vals)/len(vals))
        return res
