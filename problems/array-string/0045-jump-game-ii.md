# 45. Jump Game II

- **Difficulty:** Medium
- **Category:** Array / String
- **Tags:** Dynamic Programming, Greedy, Array

## 1. 题目描述

给定非负整数数组 nums，每个元素表示最大跳跃长度，求从起点到终点所需的最少跳跃次数。复习重点是贪心按层扩展：当前跳跃覆盖范围结束时必须跳一次，并更新下一层最远边界。

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
    def jump(self, nums: List[int]) -> int:
        jumps = end = far = 0
        for i in range(len(nums)-1):
            far = max(far, i + nums[i])
            if i == end:
                jumps += 1; end = far
        return jumps
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
print(Solution().jump([2,3,1,1,4]))  # 2
assert Solution().jump([2,3,1,1,4]) == 2
```

```text
Expected: see comments above.
```
