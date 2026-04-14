# n empty baskets
# ith basket at posui i 
# m balls need to ditrib in baskets 
# min mag force is max 






class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def helper(arr ,  mid , m):
            start = arr[0]
            m-=1
            for i in range( 1 , len(arr)):
                if arr[i] - start >= mid:
                    start = arr[i]
                    m-=1
            
            if m <= 0 :
                return True 
            else :
                return False
            
        
        position.sort()

        st = 1
        end =max(position) - min(position)
        ans = float('-inf')
        
        while st <= end:
            mid = st + (end -st)//2

            if helper(position,mid , m ) :
                ans = mid
                st = mid +1 
            else:
                end = mid - 1
            
        return ans

            