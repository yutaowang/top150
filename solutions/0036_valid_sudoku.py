from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for r in range(9):
            for c in range(9):
                v=board[r][c]
                if v!='.':
                    keys={(r,v),(v,c),(r//3,c//3,v)}
                    if seen & keys: return False
                    seen |= keys
        return True
