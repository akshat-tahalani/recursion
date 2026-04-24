class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count  = 0 
        seen =dict()
        total = 0

        for i in tasks:
            if i not in seen:
                seen[i] = 1 
            else:
                seen[i] +=1
        
        maxcount  =  max(seen.values())

        for i in seen:
            if seen[i] == maxcount :
                total +=1
            
        return max (len(tasks) ,( (maxcount - 1) * (n+1) + total))

                    