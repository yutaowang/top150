# 146. LRU Cache

- **Difficulty:** Medium
- **Category:** Linked List
- **Tags:** Linked List, Hash Table, Design

## 1. 题目描述

设计 LRUCache，支持 get 和 put，容量满时淘汰最近最少使用的键，要求 O(1) 操作。复习重点是哈希表加双向链表，访问或更新时移动到最近使用端。

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
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int): self.cap=capacity; self.od=OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.od: return -1
        self.od.move_to_end(key); return self.od[key]
    def put(self, key: int, value: int) -> None:
        if key in self.od: self.od.move_to_end(key)
        self.od[key]=value
        if len(self.od)>self.cap: self.od.popitem(last=False)
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
cache = LRUCache(2)
cache.put(1, 1); cache.put(2, 2)
print(cache.get(1))  # 1
cache.put(3, 3)
print(cache.get(2))  # -1
cache.put(4, 4)
print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4
```

```text
Expected: see comments above.
```
