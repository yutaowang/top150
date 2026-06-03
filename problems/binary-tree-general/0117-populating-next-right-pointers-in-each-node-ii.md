# 117. Populating Next Right Pointers in Each Node II

- **Difficulty:** Medium
- **Category:** Binary Tree General
- **Tags:** Depth-First Search, Linked List, Tree

## 1. 题目描述

给定二叉树，每个节点有 next 指针，要求把每层节点从左到右连接起来；若没有右侧节点则指向空。树不一定是完美二叉树。复习重点是层序遍历，或用已建立的 next 指针扫描当前层构造下一层。

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
    def connect(self, root):
        cur=root
        while cur:
            dummy=Node(0); tail=dummy
            while cur:
                for child in (cur.left, cur.right):
                    if child: tail.next=child; tail=tail.next
                cur=cur.next
            cur=dummy.next
        return root
```

## 5. 测试结果 / 简单测试例子


```python
# LeetCode 会提供 Node。
# 示例: root = [1,2,3,4,5,null,7]
# connected = Solution().connect(root)
# print(connected.val)  # 1
```

```text
Expected: see comments above.
```
