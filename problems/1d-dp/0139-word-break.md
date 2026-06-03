# 139. Word Break

- **Difficulty:** Medium
- **Category:** 1D DP
- **Tags:** Hash Table, String, Array

## 1. 题目描述

给定字符串 s 和单词字典 wordDict，判断 s 是否能被拆分成一个或多个字典中的单词。复习重点是 DP[i] 表示 s[:i] 是否可拆分。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `1D DP` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n * state)
- **空间复杂度:** O(state)

## 4. Python 代码

```python
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words=set(wordDict); dp=[False]*(len(s)+1); dp[0]=True
        for i in range(1,len(s)+1): dp[i]=any(dp[j] and s[j:i] in words for j in range(i))
        return dp[-1]
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().wordBreak("leetcode", ["leet", "code"]))  # True
assert Solution().wordBreak("leetcode", ["leet", "code"]) is True
```

```text
Expected: see comments above.
```
