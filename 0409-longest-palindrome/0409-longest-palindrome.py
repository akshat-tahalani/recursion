class Solution:
    def longestPalindrome(self, s: str) -> int:
        has_odd =False

        seen =dict()
        tsum = 0 

        for c in s:
            if c not in seen :
                seen[c] = 1
            else:
                seen[c] +=1
        

        for x in seen:
            count = seen[x]

            tsum += count // 2 * 2
            if count % 2 == 1: has_odd = True

        if has_odd : tsum+=1
        
        return tsum