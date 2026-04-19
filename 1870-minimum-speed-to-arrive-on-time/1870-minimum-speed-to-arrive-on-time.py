# hour is the amt of time to reach office 

#n trains in sequence  i +  1 adjcanebt rehne chahite asuumeinfg it breask if not adj 

#dist of lenghth n

# dist i is the dist of i th rterian 
#for two trtains to arrive int hours are allowed we have to take ceiling

#return min train travel to desti -1 if impossibe;










import math as math
class Solution:
            
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        st = 1 
        end = 10 **7
        ans  = -1
        
        if len(dist) - 1 >= hour : return -1

        def helper(arr , mid):
            thour = 0
            for i in range(len(dist) -1 ):
                
                thour += math.ceil(dist[i]/mid)
            
            thour += dist[len(dist) -1] /mid
            
            return thour

        while(st <= end):
            mid  = st + (end -st)//2

            if(helper(dist,mid) > hour ):
                
                st = mid +1  
            elif helper(dist,mid) <= hour:
                ans = mid
                end = mid -1 
            
        return ans


        