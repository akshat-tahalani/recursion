class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def helper(arr , mid ):
            out = 0
            i = 0 
            day = 1
           
            while i <len(arr) :

                if out + arr[i] > mid:
                    out = arr[i]
                    day +=1
                else:
                    out += arr[i]
                

                i+=1
            return day

        total = 0 
        ans = 0
        st = max(weights)

        for i in weights:
            total += i

        end = total

        while st <=end :
            mid = st + (end-st)//2

            if helper(weights , mid) <= days :
                ans = mid
                end = mid -1 
            else:
                st = mid+1 

        return ans

            

        
        