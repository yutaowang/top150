# 221. Maximal Square

- **Difficulty:** Medium
- **Category:** Multidimensional DP
- **Tags:** Dynamic Programming, Matrix, Array

## 1. 题目描述

给定由 0/1 字符组成的矩阵，找出只包含 1 的最大正方形面积。复习重点是 DP：若当前格为 1，则边长等于左、上、左上三个方向最小边长加 1。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

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
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0]); dp=[0]*(n+1); best=0
        for r in range(1,m+1):
            prev=0
            for c in range(1,n+1):
                tmp=dp[c]
                if matrix[r-1][c-1]=='1': dp[c]=1+min(dp[c],dp[c-1],prev); best=max(best,dp[c])
                else: dp[c]=0
                prev=tmp
        return best*best
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalSquare(matrix))  # 4
assert Solution().maximalSquare(matrix) == 4
```

```text
Expected: see comments above.
```
