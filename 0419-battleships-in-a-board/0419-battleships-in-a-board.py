class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        number = 0 
        vis = [[False]*len(board[0]) for _  in range (len(board))]

        def dfs(i , j ):
            if i < 0 or j  < 0  or i >= len(board) or j >= len(board[0]) or board[i][j] == '.' or vis[i][j] ==True:
                return 
            
            vis[i][j]  = True

            dfs(i+1 , j)
            dfs(i-1 , j)
            dfs(i , j+1)
            dfs(i , j-1)

        for i in range(len (board)):
            for j in range (len(board[0])):
                if board[i][j] == 'X' and not vis[i][j]:
                    dfs(i,j)
                    number +=1
        return number 




        