# 200. Number of Islands

- **Difficulty:** Medium
- **Category:** Graph General
- **Tags:** Breadth-First Search, Depth-First Search, Array

## 1. 题目描述

给定由 0/1 或水/陆地组成的网格，统计岛屿数量。岛屿由水平或垂直相邻的陆地连接形成。复习重点是遍历每个格子，遇到未访问陆地就 DFS/BFS 淹没整座岛。

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
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0]); ans=0
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]!='1': return
            grid[r][c]='0'
            dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1': ans+=1; dfs(r,c)
        return ans
```

## 5. 测试结果 / 简单测试例子


```python
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(Solution().numIslands(grid))  # 1
```

```text
Expected: see comments above.
```
