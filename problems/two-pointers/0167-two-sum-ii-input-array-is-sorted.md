# 167. Two Sum II - Input Array Is Sorted

- **Difficulty:** Medium
- **Category:** Two Pointers
- **Tags:** Binary Search, Two Pointers, Array

## 1. 题目描述

给定一个按非递减顺序排列的数组 numbers 和目标值 target，找出两个数使和等于 target，返回它们的 1-based 下标。题目通常保证唯一解。复习重点是排序数组上的左右双指针。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Two Pointers` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target: return [l+1, r+1]
            if s < target: l += 1
            else: r -= 1
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
print(Solution().twoSum([2,7,11,15], 9))  # [1,2]
assert Solution().twoSum([2,7,11,15], 9) == [1,2]
```

```text
Expected: see comments above.
```
