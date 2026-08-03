from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)

        @lru_cache(None)
        def maxDiff(i: int) -> int:
            if i >= n:
                return 0
            
            res = float('-inf')
            take_sum = 0
            
            # Try taking 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k - 1 < n:
                    take_sum += stoneValue[i + k - 1]
                    res = max(res, take_sum - maxDiff(i + k))
            
            return res

        diff = maxDiff(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"