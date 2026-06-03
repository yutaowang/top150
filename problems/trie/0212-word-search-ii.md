# 212. Word Search II

- **Difficulty:** Hard
- **Category:** Trie
- **Tags:** Backtracking, String, Array

## 1. 题目描述

给定字符网格和单词列表，找出所有能在网格中通过相邻格子路径组成的单词，同一单词路径不能重复使用同一格。复习重点是 Trie 存储词表，再从每个格子 DFS 剪枝搜索。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

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
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for w in words:
            node=trie
            for c in w: node=node.setdefault(c,{})
            node['$']=w
        m,n=len(board),len(board[0]); res=[]
        def dfs(r,c,node):
            ch=board[r][c]
            if ch not in node: return
            nxt=node[ch]; w=nxt.pop('$',None)
            if w: res.append(w)
            board[r][c]='#'
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and board[nr][nc]!='#': dfs(nr,nc,nxt)
            board[r][c]=ch
        for r in range(m):
            for c in range(n): dfs(r,c,trie)
        return res
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(sorted(Solution().findWords(board, words)))  # ['eat','oath']
```

```text
Expected: see comments above.
```
