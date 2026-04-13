# given array bllomday 
# int k aur int m diya hai
# m bouquets banane hai
# k adj flowers use karke 
# n flowers hai garden me and ith flower bloom karge bloom[i] din me 
# no repeteitions ek flower ek bouquet me hi use hoga
# return min num of days to make m bouquets
# if not possible return -1





# number of total flowers  = m * k 
# yaani if 
# adj flower yaani it should be while m < 0






class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def helper(arr , mid):
            counter = 0
            numbo = 0 
            for i in arr:
                if i <= mid:
                    counter+=1
                else:
                    counter=0

                if counter == k :
                    numbo +=1
                    counter = 0

            return numbo


        
        total  = m * k 
        if len(bloomDay) < total:
            return -1

        st = min(bloomDay) 
        end = max(bloomDay)
        
        ans = []


        while st <= end:
            mid = st + (end -st )//2

            if helper(bloomDay ,mid) >= m:
                ans = mid
                end = mid-1


            
            else :
                st = mid + 1
            
          
            
        return ans if ans!= -1 else -1





        