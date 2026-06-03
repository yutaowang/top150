# 208. Implement Trie (Prefix Tree)

- **Difficulty:** Medium
- **Category:** Trie
- **Tags:** Hash Table, String, Design

## 1. 题目描述

实现 Trie 前缀树，支持插入单词、查找完整单词、判断是否存在某前缀。复习重点是节点的 children 字典和 is_end 标记。

**输入/输出复习提示：** 面试时先说清楚输入类型、返回值类型、是否需要原地修改，以及是否存在空输入、重复值、越界、负数等边界情况。

> 

## 2. 解题思路

使用 `Trie` 方向的经典解法。核心目标是把状态定义清楚，然后用最直接的数据结构维护当前可行信息。对于面试，可以先说明暴力解，再说明这里的优化点。

关键步骤：

1. 明确输入边界与返回值。
2. 选择合适的数据结构或遍历顺序。
3. 在一次或有限次遍历中维护答案。
4. 对重复、空输入、边界位置做单独检查。

## 3. 复杂度分析

- **时间复杂度:** O(total characters)
- **空间复杂度:** O(total characters)

## 4. Python 代码

```python
class Trie:
    def __init__(self): self.root={}
    def insert(self, word: str) -> None:
        node=self.root
        for c in word: node=node.setdefault(c,{})
        node['#']=True
    def search(self, word: str) -> bool:
        node=self.root
        for c in word:
            if c not in node: return False
            node=node[c]
        return '#' in node
    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for c in prefix:
            if c not in node: return False
            node=node[c]
        return True
```

## 5. 测试结果 / 简单测试例子


```python
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # True
print(trie.search("app"))     # False
print(trie.startsWith("app")) # True
trie.insert("app")
print(trie.search("app"))     # True
```

```text
Expected: see comments above.
```
