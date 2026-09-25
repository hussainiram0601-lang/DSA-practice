class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        globmax,globmin = nums[0] , nums[0]
        currmax , currmin = 0,0
        total = 0
        for n in nums:
            currmax = max(currmax+n, n)
            currmin = min(currmin+n, n)
            total+=n
            globmax = max(currmax,globmax)
            globmin = min(currmin,globmin)
            
        
        return max(globmax, total-globmin) if globmax>0 else globmax
            