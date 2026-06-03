# 189. Rotate Array

- **Difficulty:** Medium
- **Category:** Array / String
- **Tags:** Two Pointers, Array, Math

## 1. 题目描述

给定数组 nums 和整数 k，把数组向右旋转 k 个位置，要求尽量原地完成。复习重点是 k 对数组长度取模，以及三次反转法：整体反转、反转前 k 段、反转后半段。

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
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums); k %= n
        nums[:] = nums[-k:] + nums[:-k]
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
nums = [1,2,3,4,5,6,7]
Solution().rotate(nums, 3)
print(nums)  # [5,6,7,1,2,3,4]
assert nums == [5,6,7,1,2,3,4]
```

```text
Expected: see comments above.
```
