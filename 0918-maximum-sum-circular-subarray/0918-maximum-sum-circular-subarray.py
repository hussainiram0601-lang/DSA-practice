class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        globalmin , globalmax = nums[0], nums[0]
        currmin , currmax = 0,0
        total = 0
        for n in nums:
            currmax = max(currmax +n , n)
            currmin = min(currmin +n , n)
            total+=n
            globalmin = min(currmin, globalmin)
            globalmax = max(globalmax, currmax)
        
        return max(globalmax, total - globalmin) if globalmax> 0 else globalmax
        