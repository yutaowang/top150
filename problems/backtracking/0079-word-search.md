# 79. Word Search

- **Difficulty:** Medium
- **Category:** Backtracking
- **Tags:** Backtracking, String, Array

## 1. 题目描述

给定字符网格 board 和字符串 word，判断 word 是否能由相邻格子的字符依次组成，同一个格子不能重复使用。复习重点是从匹配首字符的位置 DFS，并标记访问状态。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Backtracking` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** Exponential
- **空间复杂度:** O(depth)

## 4. Python 代码

```python
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        def dfs(r,c,i):
            if i==len(word): return True
            if r<0 or c<0 or r>=m or c>=n or board[r][c]!=word[i]: return False
            ch=board[r][c]; board[r][c]='#'
            ok=dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            board[r][c]=ch; return ok
        return any(dfs(r,c,0) for r in range(m) for c in range(n))
```

## 5. 测试结果 / 简单测试例子


```python
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(Solution().exist(board, "ABCCED"))  # True
assert Solution().exist(board, "ABCCED") is True
```

```text
Expected: see comments above.
```
