#array of strings 
#separator as the character
#each string is split by sperator






class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        ans = []
        word = []
        new = ''

        for  i in words :
            for char in i :
                if char == separator  :
                    
                    if ans:
                        new ="".join(ans)
                        word.append(new)
                        ans = []
                        

                else : ans.append(char)
            if ans :
                new = "".join(ans)
                word.append(new)
                ans=[]

            
            
            
        
            
        
        
       
        
        return word
            
        