#int array nums
# unt thersh
#divisor array div thgrehssold k less thn or eqal :'return ans 


import math as math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        st  = 1 
        end = max(nums)
        
        def helper(arr ,divisor):
            sum =0 
            for i in arr:
                sum += math.ceil(i / divisor)
            return sum

        while st <=end:
            divisor = st + (end - st) // 2

            if helper(nums , divisor) > threshold:
                st = divisor +1  
            elif helper(nums, divisor) <= threshold:
                ans = divisor
                end = divisor - 1 

        return ans 
                
        