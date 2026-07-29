class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjecency_list = []
        for i in range(n):
           adjecency_list.append([])
        for edge in times:
            x = edge[0]-1
            y = edge[1]-1
            w = edge[2]
            adjecency_list[x].append([y,w])
        heap = []
        dist = [float("inf")]*n
        k-=1
        dist[k] = 0
        heappush(heap,(dist[k],k))
        while len(heap)>0:
            d,u = heappop(heap)
            for v,w in adjecency_list[u]:
                if dist[u]+w < dist[v]:
                    dist[v] = dist[u]+w
                    heappush(heap , (dist[v],v))
        ans =  max(dist)
        if ans == float("inf"):
            return -1
        else:
            return ans

        