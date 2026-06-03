# 130. Surrounded Regions

- **Difficulty:** Medium
- **Category:** Graph General
- **Tags:** Breadth-First Search, Depth-First Search, Array

## 1. 题目描述

给定由 X 和 O 组成的矩阵，把所有被 X 完全包围的 O 改为 X；与边界相连的 O 不应被翻转。复习重点是从边界 O 出发标记安全区域，再翻转剩余 O。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Graph General` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(V + E)
- **空间复杂度:** O(V + E)

## 4. Python 代码

```python
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        m,n=len(board),len(board[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or board[r][c]!='O': return
            board[r][c]='E'; dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
        for r in range(m): dfs(r,0); dfs(r,n-1)
        for c in range(n): dfs(0,c); dfs(m-1,c)
        for r in range(m):
            for c in range(n): board[r][c]='O' if board[r][c]=='E' else 'X'
```

## 5. 测试结果 / 简单测试例子


```python
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)
print(board)  # [['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','O','X','X']]
```

```text
Expected: see comments above.
```
