# 82. Remove Duplicates from Sorted List II

- **Difficulty:** Medium
- **Category:** Linked List
- **Tags:** Two Pointers, Linked List

## 1. 题目描述

给定升序链表，删除所有出现重复的节点，只保留原链表中没有重复出现的数字。复习重点是 dummy 节点和前驱指针，遇到重复段要整段跳过。

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
    def deleteDuplicates(self, head):
        dummy=ListNode(0,head); prev=dummy
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val: head=head.next
                prev.next=head.next
            else: prev=prev.next
            head=head.next
        return dummy.next
```

## 5. 测试结果 / 简单测试例子


```python
# LeetCode 会提供 ListNode。
# 示例: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
# 结果应为 1 -> 2 -> 5。
# print_linked_list(Solution().deleteDuplicates(head))
```

```text
Expected: see comments above.
```
