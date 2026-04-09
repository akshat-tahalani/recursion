class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]

        for u,v in edges :
            adj[u].append(v)
            adj[v].append(u)
            

        
        vis = [0] * n

        def helper(node):
            if node == destination :
                return True

            vis[node] = 1 

            for neighbor in adj[node]:
                if vis[neighbor] == 0 :
                    if helper(neighbor):
                        return True
            
            return False
        
       
        return helper(source)