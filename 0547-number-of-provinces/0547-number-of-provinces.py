class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        province =0

        vis = [0] * n

        def dfs(city):
            vis[city] =  1

            for i in range (n):
                if vis[i] == 0 and isConnected[city][i] == 1:
                    dfs(i)
                    
        
        for city in range(n):
            if vis[city] == 0:
                dfs(city)
                province+=1

        return  province
            


        