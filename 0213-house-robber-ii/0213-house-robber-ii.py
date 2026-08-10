class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Helper function for linear House Robber
        def rob_linear(arr: List[int]) -> int:
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            
            for i in range(2, len(arr)):
                not_take = dp[i - 1]
                take = arr[i] + dp[i - 2]
                dp[i] = max(not_take, take)
                
            return dp[-1]

        # Max money from either excluding the last house or excluding the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
        