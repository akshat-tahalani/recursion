# we are expected to return a combination of 3 digit numbers that re even yaani the last digit can be only 0 2 4 6 8 
# and the other digits can be whatever 
# and the digit can be used only in the specified amount they are present 
# ek count declare karde 
# we can also use hashmap to track whther you have used the given number ? 
# how do i convert an array to a 3 digit number 




class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        
        ans = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and j!= k and i!= k:
                        d1 ,d2, d3 = digits[i] ,digits[j]  ,digits[k] 
                        if d1!=0  and d3%2== 0 :
                            ans.add(d1*100 + d2*10 + d3)
                            
                       

                    

        return len(ans)

                

            

        
        