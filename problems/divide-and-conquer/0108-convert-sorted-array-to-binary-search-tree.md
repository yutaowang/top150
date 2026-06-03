# 108. Convert Sorted Array to Binary Search Tree

- **Difficulty:** Easy
- **Category:** Divide & Conquer
- **Tags:** Divide and Conquer, Array, Tree

## 1. 题目描述

给定升序整数数组，把它转换为高度平衡的二叉搜索树。复习重点是每次选择中点作为根，递归构造左右子树。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Divide & Conquer` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n log n) typical
- **空间复杂度:** O(log n) to O(n)

## 4. Python 代码

```python
from typing import List
class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        if not nums: return None
        m=len(nums)//2; root=TreeNode(nums[m])
        root.left=self.sortedArrayToBST(nums[:m]); root.right=self.sortedArrayToBST(nums[m+1:])
        return root
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
root = Solution().sortedArrayToBST([-10,-3,0,5,9])
print(root.val)  # 通常为 0
```

```text
Expected: see comments above.
```
