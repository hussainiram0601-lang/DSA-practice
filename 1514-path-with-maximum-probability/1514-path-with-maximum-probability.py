class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src , dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src ,succProb[i]])
        pq = [(-1, start_node)]
        visited = set()
        while pq:
            prob , cur = heapq.heappop(pq)
            visited.add(cur)
            if cur == end_node:
                return -1* prob
            for neig , edgeprob in adj[cur]:
                if neig not in visited:
                    heapq.heappush(pq,(prob*edgeprob , neig))
        return 0
        