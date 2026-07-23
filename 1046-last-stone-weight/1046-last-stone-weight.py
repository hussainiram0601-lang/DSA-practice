import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for i in stones:
            heapq.heappush(h,-i)
        
        while len(h)>1:
            a= heapq.heappop(h)
            b = heapq.heappop(h)
            diff = a - b

            if diff!=0:
                heapq.heappush(h, diff)
        
        if len(h)==0:
            return 0
        
        return -h[0]
        