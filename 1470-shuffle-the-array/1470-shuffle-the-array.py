class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i  in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i+n]
        j = 2*n-1
        for i in range(n-1,-1,-1):
            y = nums[i] & (2**10-1)
            x = nums[i] >> 10
            nums[j]= y
            nums[j-1] = x
            j-=2
        return nums
        