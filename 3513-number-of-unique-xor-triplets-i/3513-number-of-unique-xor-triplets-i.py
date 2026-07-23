class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Base cases for n <= 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # For n >= 3, the result is 2^(bit_length of n)
        return 1 << n.bit_length()
        