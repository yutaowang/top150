# 399. Evaluate Division

- **Difficulty:** Medium
- **Category:** Graph General
- **Tags:** Depth-First Search, String, Array

## 1. 题目描述

给定若干除法关系 a / b = value，以及查询 x / y，返回每个查询的结果；无法推导则返回 -1。复习重点是把变量建成带权图，边权表示比例，用 DFS/BFS 累乘路径权重。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> Note: 这里是用于复习的中文转述版题意，不直接复制 LeetCode 官方原文；正式提交前可以对照官方页面确认细节。

## 2. 解题思路

使用 `Graph General` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

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
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g=defaultdict(list)
        for (a,b),v in zip(equations,values): g[a].append((b,v)); g[b].append((a,1/v))
        def bfs(s,t):
            if s not in g or t not in g: return -1.0
            q=deque([(s,1.0)]); seen={s}
            while q:
                x,val=q.popleft()
                if x==t: return val
                for y,w in g[x]:
                    if y not in seen: seen.add(y); q.append((y,val*w))
            return -1.0
        return [bfs(a,b) for a,b in queries]
```

## 5. 测试结果 / 简单测试例子

下面是最小化的复习测试代码，不使用 pytest，也不需要额外测试框架。复制到同一个文件底部，或者在 LeetCode Playground 里手动跑即可。

```python
equations = [["a","b"],["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution().calcEquation(equations, values, queries))  # [6.0,0.5,-1.0,1.0,-1.0]
```

```text
Expected: see comments above.
```
