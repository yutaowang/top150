class Solution:
    def countNodes(self, root) -> int:
        return 0 if not root else 1+self.countNodes(root.left)+self.countNodes(root.right)
