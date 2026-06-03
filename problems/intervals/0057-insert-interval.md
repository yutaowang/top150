# 57. Insert Interval

- **Difficulty:** Medium
- **Category:** Intervals
- **Tags:** Array

## 1. 题目描述

给定一组互不重叠且按起点排序的区间，以及一个新区间，把新区间插入并合并必要的重叠区间。复习重点是先加入完全在左侧的区间，再合并重叠，最后加入右侧区间。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]; i=0; n=len(intervals)
        while i<n and intervals[i][1]<newInterval[0]: res.append(intervals[i]); i+=1
        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0],intervals[i][0]); newInterval[1]=max(newInterval[1],intervals[i][1]); i+=1
        return res+[newInterval]+intervals[i:]
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
print(Solution().insert([[1,3],[6,9]], [2,5]))  # [[1,5],[6,9]]
assert Solution().insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
```

```text
Expected: see comments above.
```
