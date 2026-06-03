# 236. Lowest Common Ancestor of a Binary Tree

- **Difficulty:** Medium
- **Category:** Binary Tree General
- **Tags:** Depth-First Search, Binary Tree, Tree

## 1. 题目描述

给定二叉树根节点和两个节点 p、q，返回它们的最近公共祖先。复习重点是 DFS：若当前节点为空或等于 p/q 则返回当前；左右子树都找到则当前为 LCA。

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
    def lowestCommonAncestor(self, root, p, q):
        if not root or root in (p,q): return root
        l=self.lowestCommonAncestor(root.left,p,q); r=self.lowestCommonAncestor(root.right,p,q)
        return root if l and r else l or r
```

## 5. 测试结果 / 简单测试例子


```python
# LeetCode 会提供 TreeNode。
# 示例: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# print(Solution().lowestCommonAncestor(root, p, q).val)  # 3
```

```text
Expected: see comments above.
```
