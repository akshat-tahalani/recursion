from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh  = 0 
        q = deque()
        minutes = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2 :
                    q.append((i,j))
                
                elif grid[i][j] == 1 :
                    fresh+=1

        
        
        while len(q) != 0 and fresh > 0 :
            for _ in range(len(q)):
                i , j  = q.popleft()
                directions = [(0,1) , (0,-1), (1,0) , (-1,0)]
                for di ,dj in directions:
                    ni , nj = i+ di , j +dj
                    if 0<=ni <len(grid) and  0 <=nj<len(grid[0]) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2 
                        q.append((ni, nj))
                        fresh-=1
            minutes+=1

        return minutes if fresh == 0 else -1



        