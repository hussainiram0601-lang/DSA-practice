import bisect

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 1. Pair each value with its original index and sort by value
        sorted_nodes = sorted((val, idx) for idx, val in enumerate(nums))
        
        # Map original index to its position in the sorted array
        pos = {idx: i for i, (_, idx) in enumerate(sorted_nodes)}
        
        # 2. Compute the maximum reachable index to the right for each sorted element
        # next_jump[i] stores the index in sorted_nodes that we can jump to greedily
        next_jump = [0] * n
        for i in range(n):
            val, _ = sorted_nodes[i]
            # Find the largest element <= val + maxDiff
            idx = bisect.bisect_right(sorted_nodes, (val + maxDiff, float('inf'))) - 1
            next_jump[i] = idx

        # 3. Build Binary Lifting / Sparse Table
        # LOG represents the max power of 2 needed (2^17 > 10^5)
        LOG = 18
        up = [[i] * LOG for i in range(n)]
        
        for i in range(n):
            up[i][0] = next_jump[i]
            
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # 4. Check connectivity using prefix gaps
        # If any consecutive sorted elements have a diff > maxDiff, a boundary is formed.
        component = [0] * n
        for i in range(1, n):
            if sorted_nodes[i][0] - sorted_nodes[i-1][0] > maxDiff:
                component[i] = component[i-1] + 1
            else:
                component[i] = component[i-1]

        # 5. Process queries
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            p1, p2 = pos[u], pos[v]
            if p1 > p2:
                p1, p2 = p2, p1  # Ensure p1 is always the smaller value position
            
            # If they belong to different disconnected components
            if component[p1] != component[p2]:
                ans.append(-1)
                continue
            
            # Count the minimum jumps needed to reach or pass p2 from p1
            steps = 0
            curr = p1
            for j in range(LOG - 1, -1, -1):
                if up[curr][j] < p2:
                    curr = up[curr][j]
                    steps += (1 << j)
            
            # Since up[curr][0] >= p2, one final jump completes the path
            ans.append(steps + 1)
            
        return ans