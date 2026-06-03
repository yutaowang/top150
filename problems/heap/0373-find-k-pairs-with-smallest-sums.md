# 373. Find K Pairs with Smallest Sums

- **Difficulty:** Medium
- **Category:** Heap
- **Tags:** Heap (Priority Queue), Array

## 1. 题目描述

给定两个升序数组 nums1、nums2 和整数 k，返回和最小的 k 对数对。复习重点是最小堆从每个 nums1[i] 与 nums2[0] 的组合开始扩展。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Heap` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n log k) typical
- **空间复杂度:** O(k)

## 4. Python 代码

```python
from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        heap=[(nums1[i]+nums2[0],i,0) for i in range(min(k,len(nums1)))]
        heapq.heapify(heap); res=[]
        while heap and len(res)<k:
            _,i,j=heapq.heappop(heap); res.append([nums1[i],nums2[j]])
            if j+1<len(nums2): heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
        return res
```

## 5. 测试结果

- 本文件提供的是 LeetCode 风格提交代码。
- 数组、字符串、DP、图类题目通常可以直接复制到 LeetCode 运行。
- 链表、二叉树、Trie、设计类题目需要 LeetCode 内置的 `ListNode` / `TreeNode` / `Node` / 调用序列测试框架。
- 建议测试：官方示例 + 空输入/单元素 + 边界值 + 重复值。

```text
Status: Ready for LeetCode submission-style testing.
```
