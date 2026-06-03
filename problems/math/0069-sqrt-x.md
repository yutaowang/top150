# 69. Sqrt(x)

- **Difficulty:** Easy
- **Category:** Math
- **Tags:** Binary Search, Math

## 1. 题目描述

给定非负整数 x，返回 x 的算术平方根向下取整。复习重点是二分查找最大的 mid，使 mid*mid <= x。

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
class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        while l<=r:
            m=(l+r)//2
            if m*m<=x: ans=m; l=m+1
            else: r=m-1
        return ans
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().mySqrt(8))  # 2
assert Solution().mySqrt(8) == 2
```

```text
Expected: see comments above.
```
