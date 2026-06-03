# 103. Binary Tree Zigzag Level Order Traversal

- **Difficulty:** Medium
- **Category:** Binary Tree BFS
- **Tags:** Breadth-First Search, Binary Tree, Tree

## 1. 题目描述

给定二叉树，返回锯齿形层序遍历结果：一层从左到右，下一层从右到左交替。复习重点是 BFS 加方向标记，或双端队列。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Binary Tree BFS` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n)
- **空间复杂度:** O(w)

## 4. Python 代码

```python
from typing import List
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        if not root: return []
        q=deque([root]); res=[]; rev=False
        while q:
            level=[]
            for _ in range(len(q)):
                n=q.popleft(); level.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            res.append(level[::-1] if rev else level); rev=not rev
        return res
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
# LeetCode 会提供 TreeNode。
# 示例: root = [3,9,20,null,null,15,7]
# print(Solution().zigzagLevelOrder(root))  # [[3],[20,9],[15,7]]
```

```text
Expected: see comments above.
```
