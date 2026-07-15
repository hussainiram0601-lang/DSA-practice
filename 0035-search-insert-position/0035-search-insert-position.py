class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l , r , ans = 0, n-1, n
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>=target:
                ans = mid
                r-=1
            else:
                l = mid+1
        return ans
