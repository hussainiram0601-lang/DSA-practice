class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        r = collections.defaultdict(list)
        b = collections.defaultdict(list)
        for src , dst in redEdges:
            r[src].append(dst)
        for src , dst in blueEdges:
            b[src].append(dst)
        ans = [-1 for i in range(n)]
        q = deque()
        q.append([0 , 0 ,None])
        visited = set()
        visited.add((0,None))
        while q:
            node , lenght , color = q.popleft()
            if ans[node] == -1:
                ans[node] = lenght
            if color!='RED':
                for neig in r[node]:
                    if (neig , 'RED') not in visited:
                        visited.add((neig , 'RED'))
                        q.append([neig , lenght+1 , "RED"])
            if color!='BLUE':
                for neig in b[node]:
                    if (neig , 'BLUE') not in visited:
                        visited.add((neig , 'BLUE'))
                        q.append([neig , lenght+1 , "BLUE"])
        return ans