class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque()
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    q.append([r,c])
        
        res = -1
        direc = [[0,1], [1,0],[-1,0],[0,-1]]
        while q:
            r ,c = q.popleft()
            
            res = grid[r][c]
            
            for dr , dc in direc:
                newR , newC  = r + dr , dc +c
                if (min(newR , newC) >=0 and
                    max(newR, newC) < N and 
                    grid[newR][newC]==0):
                    q.append([newR,newC])
                    grid[newR][newC] = grid[r][c]+1

        
        return res - 1 if res>1 else -1