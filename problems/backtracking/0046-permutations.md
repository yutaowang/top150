# 46. Permutations

- **Difficulty:** Medium
- **Category:** Backtracking
- **Tags:** Backtracking, Array

## 1. 题目描述

给定不含重复数字的数组 nums，返回它的所有排列。复习重点是回溯加 used 数组/集合，路径长度等于 n 时收集答案。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Backtracking` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** Exponential
- **空间复杂度:** O(depth)

## 4. Python 代码

```python
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back(path,rem):
            if not rem: res.append(path); return
            for i,x in enumerate(rem): back(path+[x], rem[:i]+rem[i+1:])
        back([],nums); return res
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().permute([1,2,3]))  # 6 permutations
assert len(Solution().permute([1,2,3])) == 6
```

```text
Expected: see comments above.
```
