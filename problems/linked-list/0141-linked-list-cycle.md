# 141. Linked List Cycle

- **Difficulty:** Easy
- **Category:** Linked List
- **Tags:** Two Pointers, Linked List, Hash Table

## 1. 题目描述

给定链表头节点，判断链表中是否存在环。复习重点是快慢指针：快指针每次走两步，慢指针每次走一步，若相遇则有环。

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
    def hasCycle(self, head) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next; fast=fast.next.next
            if slow is fast: return True
        return False
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
# LeetCode 会提供 ListNode；本地可自己创建节点并连接成环。
a = ListNode(3); b = ListNode(2); c = ListNode(0); d = ListNode(-4)
a.next = b; b.next = c; c.next = d; d.next = b
print(Solution().hasCycle(a))  # True
```

```text
Expected: see comments above.
```
