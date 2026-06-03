class Solution:
    def construct(self, grid):
        def build(r,c,n):
            same=all(grid[i][j]==grid[r][c] for i in range(r,r+n) for j in range(c,c+n))
            if same: return Node(bool(grid[r][c]), True)
            h=n//2
            return Node(True, False, build(r,c,h), build(r,c+h,h), build(r+h,c,h), build(r+h,c+h,h))
        return build(0,0,len(grid))
