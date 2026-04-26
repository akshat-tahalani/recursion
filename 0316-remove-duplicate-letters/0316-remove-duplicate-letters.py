
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack  = []
        seen  =  dict()

        for i in s :
            if i not in seen :
                seen[i] =1 
            else :
                seen[i] +=1
            
        instack = set()
        
        
        
        for char in s :
            seen[char] -=1

            if char in instack :
                continue
            
            while stack and stack[-1]> char and seen[stack[-1]] > 0:
                yo = stack.pop()
                instack.remove(yo)
            
            instack.add(char)
            stack.append(char)
        
        return "".join(stack)
            
            
            
        
        