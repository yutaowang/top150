class Solution:
    def kthSmallest(self, root, k: int) -> int:
        st=[]
        while True:
            while root: st.append(root); root=root.left
            root=st.pop(); k-=1
            if k==0: return root.val
            root=root.right
