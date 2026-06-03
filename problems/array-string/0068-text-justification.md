# 68. Text Justification

- **Difficulty:** Hard
- **Category:** Array / String
- **Tags:** Simulation, String, Array

## 1. 题目描述

给定单词数组和每行最大宽度，把文本排版成两端对齐格式。除了最后一行或只有一个单词的行外，空格需要尽量均匀分布。复习重点是先贪心确定每行放哪些单词，再分配空格。

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
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []; i = 0
        while i < len(words):
            j = i; line_len = 0
            while j < len(words) and line_len + len(words[j]) + (j-i) <= maxWidth:
                line_len += len(words[j]); j += 1
            gaps = j - i - 1
            if j == len(words) or gaps == 0:
                line = ' '.join(words[i:j]).ljust(maxWidth)
            else:
                spaces = maxWidth - line_len; each, extra = divmod(spaces, gaps)
                line = ''.join(words[k] + ' ' * (each + (k-i < extra)) for k in range(i, j-1)) + words[j-1]
            res.append(line); i = j
        return res
```

## 5. 测试结果 / 简单测试例子


```python
words = ["This", "is", "an", "example", "of", "text", "justification."]
print(Solution().fullJustify(words, 16))
# ['This    is    an', 'example  of text', 'justification.  ']
```

```text
Expected: see comments above.
```
