# 427. Construct Quad Tree

- **Difficulty:** Medium
- **Category:** Divide & Conquer
- **Tags:** Divide and Conquer, Array, Tree

## 1. 题目描述

给定 n x n 的 0/1 网格，构造四叉树表示该区域。若一个区域所有值相同则为叶子，否则分成四个子区域递归构造。复习重点是分治判断区域是否统一。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Divide & Conquer` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n log n) typical
- **空间复杂度:** O(log n) to O(n)

## 4. Python 代码

```python
class Solution:
    def construct(self, grid):
        def build(r,c,n):
            same=all(grid[i][j]==grid[r][c] for i in range(r,r+n) for j in range(c,c+n))
            if same: return Node(bool(grid[r][c]), True)
            h=n//2
            return Node(True, False, build(r,c,h), build(r,c+h,h), build(r+h,c,h), build(r+h,c+h,h))
        return build(0,0,len(grid))
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
grid = [[0,1],[1,0]]
root = Solution().construct(grid)
print(root.isLeaf)  # False
```

```text
Expected: see comments above.
```
