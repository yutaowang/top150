# 1. Two Sum

- **Difficulty:** Easy
- **Category:** Hashmap
- **Tags:** Hash Table, Array

## 1. 题目描述

给定整数数组 nums 和目标值 target，找出两个不同下标的元素，使它们的和等于 target，并返回下标。复习重点是一次遍历哈希表记录已见过的数。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Hashmap` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n)
- **空间复杂度:** O(n)

## 4. Python 代码

```python
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,x in enumerate(nums):
            if target-x in seen: return [seen[target-x], i]
            seen[x]=i
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().twoSum([2,7,11,15], 9))  # [0,1]
assert Solution().twoSum([2,7,11,15], 9) == [0,1]
```

```text
Expected: see comments above.
```
