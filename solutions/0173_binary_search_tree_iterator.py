class BSTIterator:
    def __init__(self, root): self.st=[]; self._push(root)
    def _push(self,node):
        while node: self.st.append(node); node=node.left
    def next(self) -> int:
        node=self.st.pop(); self._push(node.right); return node.val
    def hasNext(self) -> bool: return bool(self.st)
