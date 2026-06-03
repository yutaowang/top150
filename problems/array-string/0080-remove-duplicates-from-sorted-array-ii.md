# 80. Remove Duplicates from Sorted Array II

- **Difficulty:** Medium
- **Category:** Array / String
- **Tags:** Two Pointers, Array

## 1. 题目描述

给定一个非递减排序数组 nums，原地处理重复元素，使每个元素最多出现两次，并返回处理后的长度。数组前 k 个位置应满足规则。复习重点是判断当前元素是否可以写入：只要它不同于写入区倒数第二个元素，就可以保留。

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
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if k < 2 or x != nums[k-2]:
                nums[k] = x; k += 1
        return k
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
nums = [0,0,1,1,1,1,2,3,3]
k = Solution().removeDuplicates(nums)
print(k, nums[:k])  # 7, [0,0,1,1,2,3,3]
assert k == 7
assert nums[:k] == [0,0,1,1,2,3,3]
```

```text
Expected: see comments above.
```
