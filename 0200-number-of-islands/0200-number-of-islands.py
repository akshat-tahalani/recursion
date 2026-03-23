class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        vis = [[False]*len(grid[0]) for _ in range(len(grid))]
       
        def dfs(i , j ):
            if  i < 0 or j< 0 or i >=len(grid) or j>=len(grid[0]) or grid[i][j] == '0' or vis[i][j] == True:
                return
            
            vis[i][j] = True

            dfs(i , j +1)
            dfs(i , j-1)
            dfs(i+1 , j)
            dfs(i-1, j )

        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1'  and vis[i][j] == False:
                    dfs(i,j)
                    islands+=1

        return islands

