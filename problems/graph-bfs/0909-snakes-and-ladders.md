# 909. Snakes and Ladders

- **Difficulty:** Medium
- **Category:** Graph BFS
- **Tags:** Breadth-First Search, Matrix, Array

## 1. 题目描述

给定蛇梯棋棋盘，从 1 号格出发，每次可掷 1 到 6 前进，遇到蛇或梯子必须跳转，求到达终点的最少步数。复习重点是把二维编号映射到棋盘坐标，再用 BFS 求最短步数。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Graph BFS` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(V + E)
- **空间复杂度:** O(V + E)

## 4. Python 代码

```python
from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def pos(x):
            r=(x-1)//n; c=(x-1)%n
            if r%2: c=n-1-c
            return n-1-r,c
        q=deque([(1,0)]); seen={1}
        while q:
            x,d=q.popleft()
            if x==n*n: return d
            for y in range(x+1,min(x+6,n*n)+1):
                r,c=pos(y); z=board[r][c] if board[r][c]!=-1 else y
                if z not in seen: seen.add(z); q.append((z,d+1))
        return -1
```

## 5. 测试结果

- 本文件提供的是 LeetCode 风格提交代码。
- 数组、字符串、DP、图类题目通常可以直接复制到 LeetCode 运行。
- 链表、二叉树、Trie、设计类题目需要 LeetCode 内置的 `ListNode` / `TreeNode` / `Node` / 调用序列测试框架。
- 建议测试：官方示例 + 空输入/单元素 + 边界值 + 重复值。

```text
Status: Ready for LeetCode submission-style testing.
```
