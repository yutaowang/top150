# 124. Binary Tree Maximum Path Sum

- **Difficulty:** Hard
- **Category:** Binary Tree General
- **Tags:** Dynamic Programming, Depth-First Search, Tree

## 1. 题目描述

给定非空二叉树，求任意路径的最大路径和。路径可以从任意节点开始和结束，但必须沿父子连接。复习重点是递归返回“从当前节点向下能贡献的最大单边路径”，全局更新经过当前节点的路径和。

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
    def maxPathSum(self, root) -> int:
        ans=-10**18
        def gain(node):
            nonlocal ans
            if not node: return 0
            l=max(0,gain(node.left)); r=max(0,gain(node.right))
            ans=max(ans,node.val+l+r)
            return node.val+max(l,r)
        gain(root); return ans
```

## 5. 测试结果 / 简单测试例子


```python
# LeetCode 会提供 TreeNode。
# 示例: root = [-10,9,20,null,null,15,7]
# print(Solution().maxPathSum(root))  # 42
```

```text
Expected: see comments above.
```
