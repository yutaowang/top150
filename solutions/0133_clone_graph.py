class Solution:
    def cloneGraph(self, node):
        if not node: return None
        mp={}
        def clone(n):
            if n in mp: return mp[n]
            mp[n]=Node(n.val)
            mp[n].neighbors=[clone(x) for x in n.neighbors]
            return mp[n]
        return clone(node)
