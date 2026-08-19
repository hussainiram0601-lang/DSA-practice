class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        land, borderland = 0, 0
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or not grid[r][c]:
                return 0
            
            visit.add((r, c))
            res = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
                
            return res

        for r in range(rows):
            for c in range(cols):
                land += grid[r][c]
                # Ensured proper parenthesis grouping around the boundary condition
                is_boundary = (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
                if grid[r][c] and (r, c) not in visit and is_boundary:
                    borderland += dfs(r, c)

        return land - borderland