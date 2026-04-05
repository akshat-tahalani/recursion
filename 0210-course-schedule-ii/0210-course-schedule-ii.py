class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj  = [[] for _ in range(numCourses)]
        
        
        for v , u in prerequisites:
            adj[u].append(v)
        vis = [0] * numCourses   
        pathvis = [0] * numCourses  
        stack = []

        def helper(node):
            vis[node] = 1 
            pathvis[node] =1 

            for neighbor in adj[node]:
                if vis[neighbor] == 0:
                    if helper(neighbor):
                        return True
                elif pathvis[neighbor] == 1:
                    return True
            pathvis[node] = 0
            stack.append(node)
            return False

        for i in range(numCourses):
            if vis[i] == 0 :
                if helper(i):
                    return []
        return list((reversed(stack)))

        


