# 211. Design Add and Search Words Data Structure

- **Difficulty:** Medium
- **Category:** Trie
- **Tags:** Depth-First Search, String, Design

## 1. 题目描述

设计 WordDictionary，支持添加单词和搜索模式；搜索模式中的 . 可以匹配任意单个字符。复习重点是 Trie 加 DFS 回溯处理通配符。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Trie` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(total characters)
- **空间复杂度:** O(total characters)

## 4. Python 代码

```python
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
```

## 5. 测试结果 / 简单测试例子


```python
wd = WordDictionary()
wd.addWord("bad"); wd.addWord("dad"); wd.addWord("mad")
print(wd.search("pad"))  # False
print(wd.search("bad"))  # True
print(wd.search(".ad"))  # True
print(wd.search("b.."))  # True
```

```text
Expected: see comments above.
```
