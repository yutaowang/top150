# 120. Triangle

- **Difficulty:** Medium
- **Category:** Multidimensional DP
- **Tags:** Dynamic Programming, Array

## 1. 题目描述

给定三角形数组，从顶部到底部，每步只能移动到下一行相邻位置，求路径最小和。复习重点是自底向上 DP，直接在一维数组上滚动更新。

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
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=triangle[-1][:]
        for r in range(len(triangle)-2,-1,-1):
            for c in range(len(triangle[r])): dp[c]=triangle[r][c]+min(dp[c],dp[c+1])
        return dp[0]
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle))  # 11
assert Solution().minimumTotal(triangle) == 11
```

```text
Expected: see comments above.
```
