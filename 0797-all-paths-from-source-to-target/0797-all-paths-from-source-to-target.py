# we are given a dag 
# we can use topo sort if we need 
# each index correspomds to its neighbors yes 
# so we can say that p , u , v in grapg
# and then say that adj[i] = u , v
# vis = 1
# adn then we can say that for neighbor in adj[node]:
# if neighbor == node +1 and vis == 0 

# ans.append neighbor
# helper(neighbor)
# ans.pop neighbor
# retyurn ans







class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        
        ans = []
        path = []

        

        def helper(node):

            path.append(node) 

            if node == n -1:
                ans.append(path.copy())
                path.pop()
                return 

            for neighbor in graph[node]:
                helper(neighbor)

            path.pop()
            
        
        helper(0)
        return ans

        