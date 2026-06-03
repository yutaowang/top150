# 228. Summary Ranges

- **Difficulty:** Easy
- **Category:** Intervals
- **Tags:** Array

## 1. 题目描述

给定有序且无重复的整数数组，把连续区间汇总为字符串形式。单个数字单独输出，多个连续数字输出起止范围。复习重点是扫描连续段的起点和终点。

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
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]; i=0
        while i<len(nums):
            start=nums[i]
            while i+1<len(nums) and nums[i+1]==nums[i]+1: i+=1
            res.append(str(start) if start==nums[i] else f"{start}->{nums[i]}")
            i+=1
        return res
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
print(Solution().summaryRanges([0,1,2,4,5,7]))  # ['0->2','4->5','7']
assert Solution().summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
```

```text
Expected: see comments above.
```
