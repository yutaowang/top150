# 148. Sort List

- **Difficulty:** Medium
- **Category:** Divide & Conquer
- **Tags:** Divide and Conquer, Two Pointers, Linked List

## 1. 题目描述

给定链表头节点，对链表进行升序排序，要求尽量 O(n log n) 时间和 O(1) 额外空间。复习重点是链表归并排序：快慢指针找中点，递归排序并合并。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

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
class Solution:
    def sortList(self, head):
        if not head or not head.next: return head
        slow,fast=head,head.next
        while fast and fast.next: slow=slow.next; fast=fast.next.next
        mid=slow.next; slow.next=None
        l=self.sortList(head); r=self.sortList(mid)
        dummy=cur=ListNode(0)
        while l and r:
            if l.val<r.val: cur.next,l=l,l.next
            else: cur.next,r=r,r.next
            cur=cur.next
        cur.next=l or r; return dummy.next
```

## 5. 测试结果 / 简单测试例子


```python
# LeetCode 会提供 ListNode。
# 示例: head = 4 -> 2 -> 1 -> 3
# 结果应为 1 -> 2 -> 3 -> 4。
# print_linked_list(Solution().sortList(head))
```

```text
Expected: see comments above.
```
