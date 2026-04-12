# in this question it is the first time we encounter union find 
# union find are two parameters that are used to define a representatuion of nodes
# in union is used ti cmbine the group of the gievn nodes an\
# and find uis used to define where the node vcame from that is the main parent node 
# for using union you ghave to define what find is  
# and for any question you hacve to use functions that define union and define sepaerately 







class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ans = []
        parent  = list(range(n+1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        

        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootY ==  rootX :
                return False
            
            parent[rootX] = rootY
            return True

        


        for u , v in edges:
            if not union(u,v):
                #this meaZns cycle and we should return this as teh answer
                ans.append(u)
                ans.append(v)
        
        return ans

