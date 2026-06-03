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
