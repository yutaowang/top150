class Solution:
    def maxPathSum(self, root) -> int:
        ans=-10**18
        def gain(node):
            nonlocal ans
            if not node: return 0
            l=max(0,gain(node.left)); r=max(0,gain(node.right))
            ans=max(ans,node.val+l+r)
            return node.val+max(l,r)
        gain(root); return ans
