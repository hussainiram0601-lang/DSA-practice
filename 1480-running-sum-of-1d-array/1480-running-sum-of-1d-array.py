class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        ans.append(nums[0])
        for i in range(1,n):
            r = ans[i-1] + nums[i]
            ans.append(r)
        return ans