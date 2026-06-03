# 74. Search a 2D Matrix

- **Difficulty:** Medium
- **Category:** Binary Search
- **Tags:** Binary Search, Matrix, Array

## 1. 题目描述

给定一个矩阵，每行升序，且下一行第一个元素大于上一行最后一个元素，判断 target 是否存在。复习重点是把矩阵视为一维有序数组二分。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Binary Search` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

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
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0]); l,r=0,m*n-1
        while l<=r:
            mid=(l+r)//2; v=matrix[mid//n][mid%n]
            if v==target: return True
            if v<target: l=mid+1
            else: r=mid-1
        return False
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(Solution().searchMatrix(matrix, 3))  # True
assert Solution().searchMatrix(matrix, 3) is True
```

```text
Expected: see comments above.
```
