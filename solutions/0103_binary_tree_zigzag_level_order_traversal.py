from typing import List
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        if not root: return []
        q=deque([root]); res=[]; rev=False
        while q:
            level=[]
            for _ in range(len(q)):
                n=q.popleft(); level.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            res.append(level[::-1] if rev else level); rev=not rev
        return res
