class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total_elements = m * n
        
        # Optimize k to eliminate redundant full rotations
        k = k % total_elements
        
        # Initialize a new 2D grid of the same size filled with zeros
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # Find the new 1D position after shift
                new_1d_index = (r * n + c + k) % total_elements
                
                # Convert back to 2D coordinates
                new_r = new_1d_index // n
                new_c = new_1d_index % n
                
                # Place the element in its destination
                result[new_r][new_c] = grid[r][c]
                
        return result