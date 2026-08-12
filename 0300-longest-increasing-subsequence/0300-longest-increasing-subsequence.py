class Solution:
    def lowerbound(self , nums, target):
        n = len(nums)
        l= 0
        r = n-1
        ans = n
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>=target:
                ans = mid
                r = mid - 1
            else:
                l = mid+1
        
        return ans
    def rec(self, i , prev, nums, dp):
        if i == len(nums):
            return 0
        if dp[i][prev+1]!=-1:
            return dp[i][prev+1]
        take = 0
        if prev==-1 or nums[prev]<nums[i]:
            take = 1 + self.rec(i+1,i,nums,dp)
        not_take = self.rec(i+1, prev, nums,dp)

        dp[i][prev+1]= max(take,not_take)

        return dp[i][prev+1]
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        #dp = [[-1 for _ in range(n+1)] for __ in range(n)]
        #return self.rec(0,-1,nums, dp)
        lis = []
        lis.append(nums[0])
        for i in range(1,n):
            if nums[i]>lis[-1]:
                lis.append(nums[i])
            else:
                lb  = self.lowerbound(lis, nums[i])
                lis[lb]=nums[i]
        return len(lis)