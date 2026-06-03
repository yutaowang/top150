from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        while matrix:
            res += matrix.pop(0)
            matrix = [list(row) for row in zip(*matrix)][::-1] if matrix else []
        return res
