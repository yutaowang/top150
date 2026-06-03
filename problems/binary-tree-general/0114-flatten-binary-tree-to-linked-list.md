# 114. Flatten Binary Tree to Linked List

- **Difficulty:** Medium
- **Category:** Binary Tree General
- **Tags:** Linked List, Stack, Tree

## 1. 题目描述

给定二叉树，把它原地展开为单链表，链表顺序应与前序遍历一致，所有左指针置空，右指针指向下一个节点。复习重点是后序递归拼接或迭代寻找左子树最右节点。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Binary Tree General` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

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
    def flatten(self, root) -> None:
        prev=None
        def dfs(node):
            nonlocal prev
            if not node: return
            dfs(node.right); dfs(node.left); node.right=prev; node.left=None; prev=node
        dfs(root)
```

## 5. 测试结果 / 简单测试例子


```python
# LeetCode 会提供 TreeNode。
# 示例: root = [1,2,5,3,4,null,6]
# Solution().flatten(root)
# 展平后应为 1 -> 2 -> 3 -> 4 -> 5 -> 6。
```

```text
Expected: see comments above.
```
