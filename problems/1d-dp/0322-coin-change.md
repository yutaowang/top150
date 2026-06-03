# 322. Coin Change

- **Difficulty:** Medium
- **Category:** 1D DP
- **Tags:** Breadth-First Search, Dynamic Programming, Array

## 1. 题目描述

给定硬币面额 coins 和金额 amount，求凑成 amount 所需的最少硬币数；若无法凑成返回 -1。复习重点是完全背包 DP，dp[x] 表示金额 x 的最少硬币数。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `1D DP` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n * state)
- **空间复杂度:** O(state)

## 4. Python 代码

```python
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1); dp[0]=0
        for a in range(1,amount+1):
            for c in coins:
                if c<=a: dp[a]=min(dp[a],dp[a-c]+1)
        return -1 if dp[amount]>amount else dp[amount]
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().coinChange([1,2,5], 11))  # 3
assert Solution().coinChange([1,2,5], 11) == 3
```

```text
Expected: see comments above.
```
