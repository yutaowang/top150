# 11. Container With Most Water

- **Difficulty:** Medium
- **Category:** Two Pointers
- **Tags:** Two Pointers, Greedy, Array

## 1. 题目描述

给定数组 height，每个元素表示一条竖线高度，任选两条线与 x 轴组成容器，求最大可盛水面积。复习重点是左右双指针，每次移动较短的一边。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Two Pointers` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n)
- **空间复杂度:** O(1)

## 4. Python 代码

```python
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, ans = 0, len(height)-1, 0
        while l < r:
            ans = max(ans, min(height[l], height[r])*(r-l))
            if height[l] < height[r]: l += 1
            else: r -= 1
        return ans
```

## 5. 测试结果

- 本文件提供的是 LeetCode 风格提交代码。
- 数组、字符串、DP、图类题目通常可以直接复制到 LeetCode 运行。
- 链表、二叉树、Trie、设计类题目需要 LeetCode 内置的 `ListNode` / `TreeNode` / `Node` / 调用序列测试框架。
- 建议测试：官方示例 + 空输入/单元素 + 边界值 + 重复值。

```text
Status: Ready for LeetCode submission-style testing.
```
