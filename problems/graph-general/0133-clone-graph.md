# 133. Clone Graph

- **Difficulty:** Medium
- **Category:** Graph General
- **Tags:** Breadth-First Search, Depth-First Search, Hash Table

## 1. 题目描述

给定无向连通图中的一个节点，返回整张图的深拷贝。每个节点包含值和邻居列表。复习重点是 DFS/BFS 加哈希表，避免重复复制和处理环。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

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
class Solution:
    def cloneGraph(self, node):
        if not node: return None
        mp={}
        def clone(n):
            if n in mp: return mp[n]
            mp[n]=Node(n.val)
            mp[n].neighbors=[clone(x) for x in n.neighbors]
            return mp[n]
        return clone(node)
```

## 5. 测试结果 / 简单测试例子


```python
# LeetCode 会提供 Node。
# 示例: 构造 1-2-3-4 的无向图后：
# cloned = Solution().cloneGraph(node1)
# print(cloned.val)  # 1
```

```text
Expected: see comments above.
```
