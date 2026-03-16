# the way to solve this question si by doing subtrarction of 1 or 2 from the number 
# we initially have the number and subtract 1 till we reach 0 ?
# and then we update count idk 
# what will be the recursion in this is probably like to reach n hoe many wasy aare there using 1 or 2 



from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(n):
           if n==1:
             return 1
        
           if n==2:
             return 2

      
        
        
           return helper(n-1) + helper(n-2)

        return helper(n)
       
        