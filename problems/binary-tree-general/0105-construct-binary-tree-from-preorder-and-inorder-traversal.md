# 105. Construct Binary Tree from Preorder and Inorder Traversal

- **Difficulty:** Medium
- **Category:** Binary Tree General
- **Tags:** Divide and Conquer, Hash Table, Array

## 1. 题目描述

给定 preorder 和 inorder 遍历结果，重建二叉树。假设节点值不重复。复习重点是 preorder 首元素为根，inorder 中根左侧为左子树、右侧为右子树。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

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
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        pos={v:i for i,v in enumerate(inorder)}; it=iter(preorder)
        def build(l,r):
            if l>r: return None
            v=next(it); root=TreeNode(v); m=pos[v]
            root.left=build(l,m-1); root.right=build(m+1,r); return root
        return build(0,len(inorder)-1)
```

## 5. 测试结果

- 本文件提供的是 LeetCode 风格提交代码。
- 数组、字符串、DP、图类题目通常可以直接复制到 LeetCode 运行。
- 链表、二叉树、Trie、设计类题目需要 LeetCode 内置的 `ListNode` / `TreeNode` / `Node` / 调用序列测试框架。
- 建议测试：官方示例 + 空输入/单元素 + 边界值 + 重复值。

```text
Status: Ready for LeetCode submission-style testing.
```
