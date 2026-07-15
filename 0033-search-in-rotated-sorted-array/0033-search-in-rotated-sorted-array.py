class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        # Step 1: Find the index of the minimum element (the pivot)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l  # The index of the smallest element (e.g., index of '0' in [4,5,6,7,0,1,2])
        
        # Step 2: Determine which sorted subarray contains the target
        l, r = 0, n - 1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot  # Search in the right sorted portion
        else:
            r = pivot - 1  # Search in the left sorted portion
            
        # Step 3: Perform standard binary search on the chosen portion
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return -1

        