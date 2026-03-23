from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh  = 0 #fresh oranges ka count rakha
        q = deque()#queue banai
        minutes = 0 #jo humko last me return karna hai

        for i in range(len(grid)): #pehle traverse karke append karo ki konsa konsa rotten hai
            for j in range(len(grid[0])):
                if grid[i][j] == 2 :
                    q.append((i,j))
                
                elif grid[i][j] == 1 : #mark when yiu see fresh
                    fresh+=1

        
        
        while len(q) != 0 and fresh > 0 :
            for _ in range(len(q)): #q ko traverse karenge 
                i , j  = q.popleft() #pop karte jaenge jaha jaha rotten 
                directions = [(0,1) , (0,-1), (1,0) , (-1,0)]
                for di ,dj in directions:
                    ni , nj = i+ di , j +dj
                    if 0<=ni <len(grid) and  0 <=nj<len(grid[0]) and grid[ni][nj] == 1: #if condition 
                        grid[ni][nj] = 2 #apan jo fresh hai usko rotten mark kareke queue me appnend kardo queue
                        q.append((ni, nj)) #queue me insert karte jao
                        fresh-=1  # jese hi fresh ko mark rotten kardiya wese hi num of freshhh gira do 
            minutes+=1 #har traversal par minute add ardo 

        return minutes if fresh == 0 else -1 #return minutes



        