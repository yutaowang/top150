# 295. Find Median from Data Stream

- **Difficulty:** Hard
- **Category:** Heap
- **Tags:** Two Pointers, Sorting, Design

## 1. 题目描述

设计 MedianFinder，支持动态添加数字并返回当前中位数。复习重点是双堆：最大堆保存较小一半，最小堆保存较大一半，并保持大小平衡。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

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
import heapq
class MedianFinder:
    def __init__(self): self.small=[]; self.large=[]
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num); heapq.heappush(self.large,-heapq.heappop(self.small))
        if len(self.large)>len(self.small): heapq.heappush(self.small,-heapq.heappop(self.large))
    def findMedian(self) -> float:
        return -self.small[0] if len(self.small)>len(self.large) else (-self.small[0]+self.large[0])/2
```

## 5. 测试结果 / 简单测试例子


```python
mf = MedianFinder()
mf.addNum(1); mf.addNum(2)
print(mf.findMedian())  # 1.5
mf.addNum(3)
print(mf.findMedian())  # 2.0
```

```text
Expected: see comments above.
```
