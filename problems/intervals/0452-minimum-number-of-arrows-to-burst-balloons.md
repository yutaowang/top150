# 452. Minimum Number of Arrows to Burst Balloons

- **Difficulty:** Medium
- **Category:** Intervals
- **Tags:** Sorting, Greedy, Array

## 1. 题目描述

给定气球的水平区间，每支箭在某个 x 位置射出可击穿所有覆盖该 x 的气球，求最少箭数。复习重点是按右端点排序，贪心选择当前最早结束位置射箭。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Intervals` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n log n)
- **空间复杂度:** O(n)

## 4. Python 代码

```python
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1]); arrows=0; end=None
        for a,b in points:
            if end is None or a>end:
                arrows+=1; end=b
        return arrows
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))  # 2
assert Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
```

```text
Expected: see comments above.
```
