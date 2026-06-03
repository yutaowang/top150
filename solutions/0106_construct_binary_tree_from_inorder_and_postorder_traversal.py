from typing import List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        pos={v:i for i,v in enumerate(inorder)}
        def build(l,r):
            if l>r: return None
            v=postorder.pop(); root=TreeNode(v); m=pos[v]
            root.right=build(m+1,r); root.left=build(l,m-1); return root
        return build(0,len(inorder)-1)
