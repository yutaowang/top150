# 433. Minimum Genetic Mutation

- **Difficulty:** Medium
- **Category:** Graph BFS
- **Tags:** Breadth-First Search, Hash Table, String

## 1. 题目描述

给定起始基因、目标基因和合法基因库，每次只能修改一个字符且结果必须在基因库中，求最少变换次数。复习重点是 BFS，每一步生成一位突变后的候选。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Graph BFS` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(V + E)
- **空间复杂度:** O(V + E)

## 4. Python 代码

```python
from typing import List
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank=set(bank); q=deque([(startGene,0)]); seen={startGene}
        while q:
            s,d=q.popleft()
            if s==endGene: return d
            for i in range(len(s)):
                for ch in 'ACGT':
                    t=s[:i]+ch+s[i+1:]
                    if t in bank and t not in seen: seen.add(t); q.append((t,d+1))
        return -1
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
print(Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # 1
assert Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1
```

```text
Expected: see comments above.
```
