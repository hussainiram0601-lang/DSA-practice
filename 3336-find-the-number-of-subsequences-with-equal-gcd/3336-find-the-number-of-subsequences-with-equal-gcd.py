import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        
        # dp[g1][g2] stores the number of ways to get GCD g1 for seq1 and g2 for seq2
        dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        dp[0][0] = 1
        
        # Precompute GCDs to avoid repeated math.gcd calls
        gcd_memo = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        for i in range(max_val + 1):
            for j in range(max_val + 1):
                gcd_memo[i][j] = math.gcd(i, j)
                
        for x in nums:
            # Create a copy of the current dp state
            next_dp = [row[:] for row in dp]
            
            # Transition only from reachable states
            for g1 in range(max_val + 1):
                for g2 in range(max_val + 1):
                    val = dp[g1][g2]
                    if val == 0:
                        continue
                    
                    # Case 1: Add x to the first subsequence
                    ng1 = gcd_memo[g1][x]
                    next_dp[ng1][g2] = (next_dp[ng1][g2] + val) % MOD
                    
                    # Case 2: Add x to the second subsequence
                    ng2 = gcd_memo[g2][x]
                    next_dp[g1][ng2] = (next_dp[g1][ng2] + val) % MOD
            
            dp = next_dp
            
        # Sum up all states where both are non-empty (g >= 1) and g1 == g2
        ans = 0
        for g in range(1, max_val + 1):
            ans = (ans + dp[g][g]) % MOD
            
        return ans