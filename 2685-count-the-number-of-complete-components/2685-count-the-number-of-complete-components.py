from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components_count = 0
        
        for i in range(n):
            if not visited[i]:
                # Track nodes and total edges (sum of degrees) in the current component
                component_nodes = []
                queue = [i]
                visited[i] = True
                
                # BFS to explore the component
                while queue:
                    curr = queue.pop(0)
                    component_nodes.append(curr)
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # Verify if it's a complete component
                m = len(component_nodes)
                total_degrees = sum(len(adj[node]) for node in component_nodes)
                
                # Every node in a complete component must have a degree of exactly m - 1
                if total_degrees == m * (m - 1):
                    complete_components_count += 1
                    
        return complete_components_count