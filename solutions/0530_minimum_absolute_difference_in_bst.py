class Solution:
    def getMinimumDifference(self, root) -> int:
        prev=None; ans=float('inf')
        def dfs(node):
            nonlocal prev, ans
            if not node: return
            dfs(node.left)
            if prev is not None: ans=min(ans,node.val-prev)
            prev=node.val
            dfs(node.right)
        dfs(root); return ans
