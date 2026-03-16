class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        if n == 0 :
            return 

        evenposi = (n+1 )// 2 

        oddposi = n//2 
        mod = 10**9 + 7

        ans = pow( 5 , evenposi ,mod) * pow( 4  , oddposi ,mod)
        return ans  % mod
