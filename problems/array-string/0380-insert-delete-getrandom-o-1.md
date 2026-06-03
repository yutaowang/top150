# 380. Insert Delete GetRandom O(1)

- **Difficulty:** Medium
- **Category:** Array / String
- **Tags:** Hash Table, Array, Math

## 1. 题目描述

设计 RandomizedSet，支持 insert、remove、getRandom，要求平均 O(1) 时间。复习重点是数组存储元素、哈希表记录元素下标，删除时把末尾元素交换到被删位置。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Array / String` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n) typical
- **空间复杂度:** O(1) to O(n)

## 4. Python 代码

```python
import random

class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.pos = {}
    def insert(self, val: int) -> bool:
        if val in self.pos: return False
        self.pos[val] = len(self.arr); self.arr.append(val); return True
    def remove(self, val: int) -> bool:
        if val not in self.pos: return False
        i = self.pos.pop(val); last = self.arr.pop()
        if i < len(self.arr):
            self.arr[i] = last; self.pos[last] = i
        return True
    def getRandom(self) -> int:
        return random.choice(self.arr)
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
obj = RandomizedSet()
print(obj.insert(1))   # True
print(obj.remove(2))   # False
print(obj.insert(2))   # True
print(obj.getRandom()) # 1 or 2
print(obj.remove(1))   # True
print(obj.insert(2))   # False
```

```text
Expected: see comments above.
```
