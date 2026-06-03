# 72. Edit Distance

- **Difficulty:** Medium
- **Category:** Multidimensional DP
- **Tags:** Dynamic Programming, String

## 1. 题目描述

给定两个单词 word1 和 word2，求把 word1 转换成 word2 的最少操作数，允许插入、删除、替换一个字符。复习重点是编辑距离 DP。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Multidimensional DP` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(mn) typical
- **空间复杂度:** O(mn) or optimized

## 4. Python 代码

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2); dp=list(range(n+1))
        for i in range(1,m+1):
            prev,dp[0]=dp[0],i
            for j in range(1,n+1):
                tmp=dp[j]
                dp[j]=prev if word1[i-1]==word2[j-1] else 1+min(prev,dp[j],dp[j-1])
                prev=tmp
        return dp[-1]
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().minDistance("horse", "ros"))  # 3
assert Solution().minDistance("horse", "ros") == 3
```

```text
Expected: see comments above.
```
