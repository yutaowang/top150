# 199. Binary Tree Right Side View

- **Difficulty:** Medium
- **Category:** Binary Tree BFS
- **Tags:** Breadth-First Search, Depth-First Search, Tree

## 1. 题目描述

给定二叉树，返回从右侧观察时每一层能看到的节点值。复习重点是 BFS 每层取最后一个节点，或 DFS 优先访问右子树并记录每层第一个节点。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

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
    def rightSideView(self, root) -> List[int]:
        if not root: return []
        q=deque([root]); res=[]
        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                n=q.popleft()
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
        return res
```

## 5. 测试结果 / 简单测试例子


```python
# LeetCode 会提供 TreeNode。
# 示例: root = [1,2,3,null,5,null,4]
# print(Solution().rightSideView(root))  # [1,3,4]
```

```text
Expected: see comments above.
```
