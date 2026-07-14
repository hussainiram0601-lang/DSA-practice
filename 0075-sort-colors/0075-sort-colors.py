class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        mx = max(nums)
        freq = [0]*(mx+1)
        for i in nums:
            freq[i]+=1

        idx = 0
        for i in range(0,mx+1):
            while freq[i]>0:
                nums[idx]=i
                idx+=1
                freq[i]-=1

        