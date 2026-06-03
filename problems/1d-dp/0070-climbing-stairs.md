# 70. Climbing Stairs

- **Difficulty:** Easy
- **Category:** 1D DP
- **Tags:** Dynamic Programming, Memoization, Math

## 1. 题目描述

给定楼梯层数 n，每次可以爬 1 或 2 阶，求到达顶部的不同方法数。复习重点是斐波那契型 DP。

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
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,1
        for _ in range(n): a,b=b,a+b
        return a
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().climbStairs(3))  # 3
assert Solution().climbStairs(3) == 3
```

```text
Expected: see comments above.
```
