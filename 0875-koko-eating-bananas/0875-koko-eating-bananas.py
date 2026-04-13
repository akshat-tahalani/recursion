# esa kar ki max aur min decided hai per hour tu kitne khaa sakta

# min would be the smallest value of bananas and max will be max of theta array 

# lets do i would say ah lpeer function 

# what will that helper function help ?

# esa function if :


import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def helper(arr ,mid):

            hours = 0
            i  =0 

            for bana in piles:
                hours += math.ceil(bana / mid)
            return hours

        
        st = 1
        end = max(piles)
        ans = 0 

        while st<=end:
            mid = st +(end-st)//2

            hourss = helper(piles , mid)

            if hourss <= h :
                ans = mid
                end = mid -1
                
                

            else:
                st = mid +1  
        
        return ans 

