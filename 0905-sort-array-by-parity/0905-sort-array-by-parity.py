class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                temp = nums[start]
                nums[start] = nums[i]
                nums[i]= temp
                start+=1
        return nums