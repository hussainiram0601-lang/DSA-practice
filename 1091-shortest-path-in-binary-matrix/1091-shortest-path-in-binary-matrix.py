class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        N= len(grid)
        visit = set()
        q = deque([(0,0,1)])
        direct = [[0,1],[1,0],[-1,0],[0,-1],[1,-1],[-1,1],[-1,-1],[1,1]]
        while q:
            r,c,l= q.popleft()
            if (max(r,c)>=N or min(r,c)<0 or grid[r][c]):
                continue
            if r==N-1 and c == N-1:
                return l

            for dr, dc in direct:
                if ((r+dr, c+dc)) not in visit:
                    q.append((dr+r,dc+c,l+1))
                    visit.add((dr+r,dc+c))
        return -1
