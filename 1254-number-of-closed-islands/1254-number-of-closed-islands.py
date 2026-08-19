class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visit = set()
        res=0
        def dfs(r,c):
            if (r<0 or c<0 or r==rows or c==cols):
                return 0
            if grid[r][c]==1 or (r,c)  in visit:
                return 1
            visit.add((r,c))
            return min(
                dfs(r+1,c),
                dfs(r,c+1),
                dfs(r-1,c),
                dfs(r,c-1)
            ) 
        for r in range(rows):
            for c in range(cols):
                if not grid[r][c] and (r,c) not in visit:
                    res+=dfs(r,c)
        return res