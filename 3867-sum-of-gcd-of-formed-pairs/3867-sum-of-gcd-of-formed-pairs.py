import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        
        # Step 1: Construct prefixGcd array
        mx = 0
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(math.gcd(num, mx))
            
        # Step 2: Sort prefixGcd in non-decreasing order
        prefixGcd.sort()
        
        # Step 3: Form pairs using two pointers and sum their GCDs
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum
        