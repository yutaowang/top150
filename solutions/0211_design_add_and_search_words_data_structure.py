class WordDictionary:
    def __init__(self): self.root={}
    def addWord(self, word: str) -> None:
        node=self.root
        for c in word: node=node.setdefault(c,{})
        node['#']=True
    def search(self, word: str) -> bool:
        def dfs(i,node):
            if i==len(word): return '#' in node
            c=word[i]
            if c=='.': return any(k!='#' and dfs(i+1,v) for k,v in node.items())
            return c in node and dfs(i+1,node[c])
        return dfs(0,self.root)
