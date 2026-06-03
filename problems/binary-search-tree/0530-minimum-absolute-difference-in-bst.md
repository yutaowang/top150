# 530. Minimum Absolute Difference in BST

- **Difficulty:** Easy
- **Category:** Binary Search Tree
- **Tags:** Breadth-First Search, Depth-First Search, Tree

## 1. 题目描述

给定二叉搜索树，求任意两个不同节点值之间的最小绝对差。复习重点是 BST 中序遍历得到递增序列，只需比较相邻值。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Binary Search Tree` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n)
- **空间复杂度:** O(h)

## 4. Python 代码

```python
class Solution:
    def getMinimumDifference(self, root) -> int:
        prev=None; ans=float('inf')
        def dfs(node):
            nonlocal prev, ans
            if not node: return
            dfs(node.left)
            if prev is not None: ans=min(ans,node.val-prev)
            prev=node.val
            dfs(node.right)
        dfs(root); return ans
```

## 5. 测试结果 / 简单测试例子


```python
# LeetCode 会提供 TreeNode。
# 示例: root = [4,2,6,1,3]
# print(Solution().getMinimumDifference(root))  # 1
```

```text
Expected: see comments above.
```
