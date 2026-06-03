from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        pos={v:i for i,v in enumerate(inorder)}; it=iter(preorder)
        def build(l,r):
            if l>r: return None
            v=next(it); root=TreeNode(v); m=pos[v]
            root.left=build(l,m-1); root.right=build(m+1,r); return root
        return build(0,len(inorder)-1)
