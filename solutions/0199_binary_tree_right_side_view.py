from typing import List
from collections import deque
class Solution:
    def rightSideView(self, root) -> List[int]:
        if not root: return []
        q=deque([root]); res=[]
        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                n=q.popleft()
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
        return res
