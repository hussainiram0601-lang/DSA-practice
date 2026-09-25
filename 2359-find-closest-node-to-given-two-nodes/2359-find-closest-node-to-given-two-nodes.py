class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        adj = collections.defaultdict(list)
        for i, dst in enumerate(edges):
            adj[i].append(dst)

        def bfs(src , distMap):
            q = deque()
            q.append([src,0])
            distMap[src] =0
            while q:
                node , dist = q.popleft()
                for neig  in adj[node]:
                    if neig not in distMap:
                        q.append([neig , dist+1])
                        distMap[neig] = dist+1

        

        node1Dist = {}
        node2Dist = {}
        bfs(node1 ,node1Dist)
        bfs(node2 ,node2Dist)
        res = -1
        resDist = float("inf")
        for i in range(len(edges)):
            if i  in node1Dist and i in node2Dist:
                dist = max(node1Dist[i], node2Dist[i])
                if dist <resDist:
                    res=i
                    resDist = dist
        return res