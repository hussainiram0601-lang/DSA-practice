class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        
        # The length of the sequential number can range from 2 to 9 digits
        for length in range(2, 10):
            # Slide the window across the digits string
            for start in range(10 - length):
                substring = digits[start : start + length]
                num = int(substring)
                
                # Check if it fits the range constraints
                if low <= num <= high:
                    result.append(num)
                elif num > high:
                    # Since numbers are strictly increasing, we can stop early 
                    # if the current number exceeds the high limit.
                    break
                    
        return result
        