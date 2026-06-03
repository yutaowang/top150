# 224. Basic Calculator

- **Difficulty:** Hard
- **Category:** Stack
- **Tags:** String, Stack, Math

## 1. 题目描述

给定包含整数、加减号、括号和空格的表达式字符串，计算其值。复习重点是处理括号带来的符号环境，可用栈保存进入括号前的结果和符号。

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
class Solution:
    def calculate(self, s: str) -> int:
        ans=num=0; sign=1; st=[]
        for c in s:
            if c.isdigit(): num=num*10+int(c)
            elif c in '+-':
                ans += sign*num; num=0; sign=1 if c=='+' else -1
            elif c=='(': st.append((ans,sign)); ans=0; sign=1
            elif c==')':
                ans += sign*num; num=0; prev,psign=st.pop(); ans=prev+psign*ans
        return ans + sign*num
```

## 5. 测试结果 / 简单测试例子


```python
print(Solution().calculate("1 + 1"))  # 2
assert Solution().calculate("1 + 1") == 2
```

```text
Expected: see comments above.
```
