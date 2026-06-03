# 55. Jump Game

- **Difficulty:** Medium
- **Category:** Array / String
- **Tags:** Dynamic Programming, Greedy, Array

## 1. 题目描述

给定非负整数数组 nums，每个元素表示从该位置最多能跳多远，判断是否能从下标 0 到达最后一个下标。复习重点是维护当前能到达的最远位置，若当前位置超过最远位置则失败。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Array / String` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n) typical
- **空间复杂度:** O(1) to O(n)

## 4. Python 代码

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i, jump in enumerate(nums):
            if i > far: return False
            far = max(far, i + jump)
        return True
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().canJump([2,3,1,1,4]))  # True
assert Solution().canJump([2,3,1,1,4]) is True
```

```text
Expected: see comments above.
```
