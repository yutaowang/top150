# 210. Course Schedule II

- **Difficulty:** Medium
- **Category:** Graph General
- **Tags:** Breadth-First Search, Depth-First Search, Graph Theory

## 1. 题目描述

Solve LeetCode #210 (Course Schedule II). This file gives a concise paraphrase of the task and focuses on the algorithm, implementation, and test strategy.

> Note: 为避免直接复制 LeetCode 原题文本，这里使用简要转述。提交前可对照 LeetCode 官方页面确认输入输出细节。

## 2. 解题思路

使用 `Graph General` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

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
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g=defaultdict(list); indeg=[0]*numCourses
        for a,b in prerequisites: g[b].append(a); indeg[a]+=1
        q=deque([i for i,d in enumerate(indeg) if d==0]); order=[]
        while q:
            x=q.popleft(); order.append(x)
            for y in g[x]:
                indeg[y]-=1
                if indeg[y]==0: q.append(y)
        return order if len(order)==numCourses else []
```

## 5. 测试结果

- 本文件提供的是 LeetCode 风格提交代码。
- 数组、字符串、DP、图类题目通常可以直接复制到 LeetCode 运行。
- 链表、二叉树、Trie、设计类题目需要 LeetCode 内置的 `ListNode` / `TreeNode` / `Node` / 调用序列测试框架。
- 建议测试：官方示例 + 空输入/单元素 + 边界值 + 重复值。

```text
Status: Ready for LeetCode submission-style testing.
```
