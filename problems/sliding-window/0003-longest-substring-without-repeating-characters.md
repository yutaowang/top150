# 3. Longest Substring Without Repeating Characters

- **Difficulty:** Medium
- **Category:** Sliding Window
- **Tags:** Sliding Window, Hash Table, String

## 1. 题目描述

给定字符串 s，求不含重复字符的最长子串长度。复习重点是滑动窗口加哈希集合/下标表，遇到重复字符时移动左边界。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Sliding Window` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n)
- **空间复杂度:** O(k)

## 4. Python 代码

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}; l=ans=0
        for r,c in enumerate(s):
            if c in seen and seen[c]>=l: l=seen[c]+1
            seen[c]=r; ans=max(ans,r-l+1)
        return ans
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
```

```text
Expected: see comments above.
```
