class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ans = 0 
        differences = []

        for i in range(len(capacity) ):
            differences.append(capacity[i] - rocks[i]) 

        differences.sort()



        for i in range(len(capacity)):
            

            if differences[i]== 0 :
                ans +=1
            
            elif  differences[i] != 0 and differences[i] <= additionalRocks:
                additionalRocks -= differences[i]
                ans +=1
            
        return ans
        