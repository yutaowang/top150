# 97. Interleaving String

- **Difficulty:** Medium
- **Category:** Multidimensional DP
- **Tags:** Dynamic Programming, String

## 1. 题目描述

给定字符串 s1、s2、s3，判断 s3 是否由 s1 和 s2 交错组成，同时保持 s1、s2 内部字符相对顺序。复习重点是二维 DP，dp[i][j] 表示 s1 前 i 个和 s2 前 j 个能否组成 s3 前 i+j 个。

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
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3): return False
        dp=[False]*(len(s2)+1); dp[0]=True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==j==0: continue
                dp[j]=(i>0 and dp[j] and s1[i-1]==s3[i+j-1]) or (j>0 and dp[j-1] and s2[j-1]==s3[i+j-1])
        return dp[-1]
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True
assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
```

```text
Expected: see comments above.
```
