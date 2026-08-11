class Solution:
    def rec(self, i , sum1 , nums, total,dp):
        if sum1>(total//2):
            return False
        elif sum1 == (total//2):
            return True
        elif i== len(nums):
            return False
        
        if dp[i][sum1]!=-1:
            return dp[i][sum1]

        take = self.rec(i+1, sum1+nums[i], nums , total,dp)
        not_take = self.rec(i+1, sum1, nums, total,dp)
        dp[i][sum1]= take or not_take
        return dp[i][sum1]
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if len(nums)==1:
            return False
        if total%2==1:
            return False
        dp = [[-1 for j in range((total//2)+1)] for i in range(len(nums))]
        return self.rec( 0,0 ,nums , total,dp)
        