# 150. Evaluate Reverse Polish Notation

- **Difficulty:** Medium
- **Category:** Stack
- **Tags:** Array, Stack, Math

## 1. 题目描述

给定逆波兰表达式 tokens，计算表达式值。操作数在前，运算符在后，支持四则运算。复习重点是栈遇数字入栈，遇操作符弹出两个数计算后压回。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Stack` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

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
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for t in tokens:
            if t not in '+-*/': st.append(int(t)); continue
            b,a=st.pop(),st.pop()
            st.append(a+b if t=='+' else a-b if t=='-' else a*b if t=='*' else int(a/b))
        return st[-1]
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().evalRPN(["2","1","+","3","*"]))  # 9
assert Solution().evalRPN(["2","1","+","3","*"]) == 9
```

```text
Expected: see comments above.
```
