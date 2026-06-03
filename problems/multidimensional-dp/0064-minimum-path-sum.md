# 64. Minimum Path Sum

- **Difficulty:** Medium
- **Category:** Multidimensional DP
- **Tags:** Dynamic Programming, Matrix, Array

## 1. 题目描述

给定 m x n 网格，每个格子有非负权重，从左上角到右下角只能向右或向下移动，求路径最小和。复习重点是二维/一维 DP。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Multidimensional DP` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(mn) typical
- **空间复杂度:** O(mn) or optimized

## 4. Python 代码

```python
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        for r in range(m):
            for c in range(n):
                if r==c==0: continue
                grid[r][c]+=min(grid[r-1][c] if r else float('inf'), grid[r][c-1] if c else float('inf'))
        return grid[-1][-1]
```

## 5. 测试结果 / 简单测试例子


```python
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum(grid))  # 7
assert Solution().minPathSum(grid) == 7
```

```text
Expected: see comments above.
```
