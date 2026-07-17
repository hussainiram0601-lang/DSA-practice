import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Step 1: Count frequency of each number
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        # Count how many numbers are multiples of each i
        cnt = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                cnt[i] += freq[j]
                
        # Step 2 & 3: Compute exact gcd counts using inclusion-exclusion backwards
        gcd_counts = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            # Total pairs that have 'i' as a common divisor
            total_pairs = (cnt[i] * (cnt[i] - 1)) // 2
            
            # Subtract pairs that have a larger multiple of 'i' as their actual GCD
            minus = 0
            for j in range(2 * i, max_val + 1, i):
                minus += gcd_counts[j]
                
            gcd_counts[i] = total_pairs - minus
            
        # Step 4: Build prefix sums of counts to find boundaries
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + gcd_counts[i]
            
        # Answer each query using binary search
        ans = []
        for q in queries:
            # We want to find the first index where prefix_sums[idx] > q
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans
        