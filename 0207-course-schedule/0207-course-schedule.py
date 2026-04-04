class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for v , u in prerequisites:
            adj[v].append(u)
        
        vis = [0]* numCourses 

        def helper(node) :

            vis[node] = 1 

            for neighbor in adj[node]:
                if vis[neighbor]==1 :
                    return True
                elif vis[neighbor] ==  0:
                    if helper(neighbor): return True
            vis[node] = 2
            return False

        for i in range(numCourses):
            if vis[i] == 0 :
                if helper(i): return False
        return True
        