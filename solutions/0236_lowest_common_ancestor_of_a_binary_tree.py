class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root in (p,q): return root
        l=self.lowestCommonAncestor(root.left,p,q); r=self.lowestCommonAncestor(root.right,p,q)
        return root if l and r else l or r
