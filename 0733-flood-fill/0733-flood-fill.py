class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        vis = [[0] * len(image[0]) for _  in range (len(image))]
        og_color = image[sr][sc]

        def helper(i,j):
             

            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or vis[i][j]==1 or image[i][j] == color or image[i][j] != og_color :
                return
            
            vis[i][j] = 1

            image[i][j] = color

            helper(i+1 , j)
            helper(i , j-1)
            helper(i , j+1)
            helper(i-1 , j)
        
        helper(sr ,sc)
        return image            

            
        