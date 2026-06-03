# 73. Set Matrix Zeroes

- **Difficulty:** Medium
- **Category:** Matrix
- **Tags:** Hash Table, Matrix, Array

## 1. 题目描述

给定矩阵，如果某个元素为 0，则把它所在的整行和整列都设为 0，要求尽量原地完成。复习重点是用第一行和第一列作为标记，并额外记录它们自身是否需要置零。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

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
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0]); first_col=any(matrix[i][0]==0 for i in range(m))
        first_row=any(matrix[0][j]==0 for j in range(n))
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0: matrix[i][0]=matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0: matrix[i][j]=0
        if first_row: matrix[0]=[0]*n
        if first_col:
            for i in range(m): matrix[i][0]=0
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)
print(matrix)  # [[1,0,1],[0,0,0],[1,0,1]]
```

```text
Expected: see comments above.
```
