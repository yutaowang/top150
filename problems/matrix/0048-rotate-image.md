# 48. Rotate Image

- **Difficulty:** Medium
- **Category:** Matrix
- **Tags:** Matrix, Array, Math

## 1. 题目描述

给定 n x n 矩阵，把图像顺时针旋转 90 度，要求原地修改。复习重点是先转置再水平翻转，或按层四点交换。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Matrix` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(mn)
- **空间复杂度:** O(1) to O(mn)

## 4. Python 代码

```python
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n): matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix: row.reverse()
```

## 5. 测试结果 / 简单测试例子


```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)
print(matrix)  # [[7,4,1],[8,5,2],[9,6,3]]
```

```text
Expected: see comments above.
```
