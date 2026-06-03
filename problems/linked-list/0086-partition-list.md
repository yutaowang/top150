# 86. Partition List

- **Difficulty:** Medium
- **Category:** Linked List
- **Tags:** Two Pointers, Linked List

## 1. 题目描述

给定链表和整数 x，把所有小于 x 的节点放到大于等于 x 的节点之前，同时保持两部分内部相对顺序。复习重点是两个 dummy 链表分别收集小于和大于等于的节点。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Linked List` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n)
- **空间复杂度:** O(1) to O(n)

## 4. Python 代码

```python
class Solution:
    def partition(self, head, x: int):
        before=bt=ListNode(0); after=at=ListNode(0)
        while head:
            if head.val < x: bt.next=head; bt=bt.next
            else: at.next=head; at=at.next
            head=head.next
        at.next=None; bt.next=after.next
        return before.next
```

## 5. 测试结果 / 简单测试例子


```python
# LeetCode 会提供 ListNode。
# 示例: head = 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
# 结果应为 1 -> 2 -> 2 -> 4 -> 3 -> 5。
# print_linked_list(Solution().partition(head, 3))
```

```text
Expected: see comments above.
```
