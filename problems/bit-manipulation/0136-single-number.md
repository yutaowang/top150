# 136. Single Number

- **Difficulty:** Easy
- **Category:** Bit Manipulation
- **Tags:** Bit Manipulation, Array

## 1. 题目描述

给定非空整数数组，除一个元素只出现一次外，其余元素都出现两次，找出只出现一次的元素。复习重点是异或运算：相同数异或为 0，0 异或任何数为其本身。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Bit Manipulation` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n) or O(1)
- **空间复杂度:** O(1)

## 4. Python 代码

```python
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for x in nums: ans ^= x
        return ans
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().singleNumber([4,1,2,1,2]))  # 4
assert Solution().singleNumber([4,1,2,1,2]) == 4
```

```text
Expected: see comments above.
```
