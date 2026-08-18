class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res =[]
        potions.sort()
        
        for s in spells:
            l,r = 0, len(potions)-1
            idx = len(potions)
            while l <=r:
                mid = (l+r)//2
                
                if s*potions[mid] >= success:
                    r = mid-1
                    idx = mid
                else:
                    l = mid+1
            res.append(len(potions) - idx)
        return res
        