# 149. Max Points on a Line

- **Difficulty:** Hard
- **Category:** Math
- **Tags:** Hash Table, Array, Math

## 1. 题目描述

给定平面上的若干点，求最多有多少点在同一条直线上。复习重点是枚举每个点作为基准，统计与其他点形成的斜率，斜率用约分后的 dy/dx 表示。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Math` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(log n) typical
- **空间复杂度:** O(1)

## 4. Python 代码

```python
from typing import List
from collections import defaultdict
from math import gcd
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2: return len(points)
        ans=0
        for i,(x1,y1) in enumerate(points):
            cnt=defaultdict(int)
            for x2,y2 in points[i+1:]:
                dx,dy=x2-x1,y2-y1; g=gcd(dx,dy); cnt[(dx//g,dy//g)] += 1
            ans=max(ans, 1 + (max(cnt.values()) if cnt else 0))
        return ans
```

## 5. 测试结果 / 简单测试例子


```python
points = [[1,1],[2,2],[3,3]]
print(Solution().maxPoints(points))  # 3
assert Solution().maxPoints(points) == 3
```

```text
Expected: see comments above.
```
