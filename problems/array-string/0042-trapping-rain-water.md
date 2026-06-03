# 42. Trapping Rain Water

- **Difficulty:** Hard
- **Category:** Array / String
- **Tags:** Dynamic Programming, Two Pointers, Array

## 1. 题目描述

给定每个位置的柱子高度，计算下雨后能接住多少水。复习重点是每个位置的蓄水量由左侧最高和右侧最高的较小值决定；可用双指针优化空间。

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
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1; lm = rm = ans = 0
        while l < r:
            if height[l] < height[r]:
                lm = max(lm, height[l]); ans += lm - height[l]; l += 1
            else:
                rm = max(rm, height[r]); ans += rm - height[r]; r -= 1
        return ans
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
```

```text
Expected: see comments above.
```
