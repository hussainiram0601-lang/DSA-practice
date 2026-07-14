class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = n-1
        i = 0
        while i<=r:
            if nums[i]==1:
                i+=1
            elif nums[i]==0:
                temp = nums[i]
                nums[i]=nums[l]
                nums[l]=temp
                i+=1
                l+=1
            else:
                temp= nums[i]
                nums[i]= nums[r]
                nums[r]=temp
                r-=1

        