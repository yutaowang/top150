# 205. Isomorphic Strings

- **Difficulty:** Easy
- **Category:** Hashmap
- **Tags:** Hash Table, String

## 1. 题目描述

给定两个字符串 s 和 t，判断它们是否同构：s 中每个字符能唯一映射到 t 中一个字符，并保持顺序结构。复习重点是双向映射，防止多个字符映射到同一个字符。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Hashmap` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(n)
- **空间复杂度:** O(n)

## 4. Python 代码

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().isIsomorphic("egg", "add"))  # True
assert Solution().isIsomorphic("egg", "add") is True
```

```text
Expected: see comments above.
```
