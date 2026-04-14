import math as math
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def helper(arr,mid):
            # we have to traveerse the arr and divide the products 
            stores = 0
            
            for i in arr:
                stores += math.ceil(i/mid)
                
            return stores



        
        fin =0
        st = 1
        #the number of prod is the nmid we use to binary search 
        end = max(quantities)

        while  st <=end:
            mid = st + (end - st)//2

            if helper(quantities ,mid) > n:
                st = mid +1
            else:
                fin= mid 
                end = mid -1
        return fin 