# 21. Merge Two Sorted Lists

- **Difficulty:** Easy
- **Category:** Linked List
- **Tags:** Linked List, Recursion

## 1. 题目描述

给定两个升序链表，合并成一个升序链表并返回头节点。复习重点是 dummy 节点加双指针，逐步接入较小节点。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

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
    def mergeTwoLists(self, list1, list2):
        dummy=cur=ListNode(0)
        while list1 and list2:
            if list1.val < list2.val: cur.next,list1=list1,list1.next
            else: cur.next,list2=list2,list2.next
            cur=cur.next
        cur.next=list1 or list2
        return dummy.next
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
# LeetCode 会提供 ListNode。
# 示例: 1 -> 2 -> 4 与 1 -> 3 -> 4 合并后应为 1 -> 1 -> 2 -> 3 -> 4 -> 4。
# print_linked_list(Solution().mergeTwoLists(list1, list2))
```

```text
Expected: see comments above.
```
