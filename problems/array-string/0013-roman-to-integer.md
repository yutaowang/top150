# 13. Roman to Integer

- **Difficulty:** Easy
- **Category:** Array / String
- **Tags:** Hash Table, String, Math

## 1. 题目描述

给定一个罗马数字字符串，把它转换为整数。复习重点是当小值出现在大值左边时表示减法，否则表示加法。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

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
class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        for i, ch in enumerate(s):
            ans += -val[ch] if i+1 < len(s) and val[ch] < val[s[i+1]] else val[ch]
        return ans
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().romanToInt("MCMXCIV"))  # 1994
assert Solution().romanToInt("MCMXCIV") == 1994
```

```text
Expected: see comments above.
```
