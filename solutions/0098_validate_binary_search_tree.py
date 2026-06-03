class Solution:
    def isValidBST(self, root) -> bool:
        def ok(node, lo, hi):
            if not node: return True
            return lo < node.val < hi and ok(node.left, lo, node.val) and ok(node.right, node.val, hi)
        return ok(root, float('-inf'), float('inf'))
