# 53. Maximum Subarray

- **Difficulty:** Medium
- **Category:** Kadane's Algorithm
- **Tags:** Dynamic Programming, Divide and Conquer, Array

## 1. 题目描述

给定整数数组 nums，找出和最大的连续子数组并返回其和。复习重点是 Kadane 算法：当前和若为负则从当前元素重新开始。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Kadane's Algorithm` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n)
- **空间复杂度:** O(1)

## 4. Python 代码

```python
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=cur=nums[0]
        for x in nums[1:]: cur=max(x,cur+x); best=max(best,cur)
        return best
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
```

```text
Expected: see comments above.
```
