class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count  = 0 
        seen =dict()
        total = 0

        #my intuition was right to use hjasmpas to track the frequency of tasks
        #in thi s question our entire formula depends upon the the most frequent element 
        #so the intervals and the n is going to cvhange the output because of the most freq elemnets 
        #then we try to hit and trial the formula of the intervals
        #then at the ned we have to make sure the intervals are more than the length of the number 
        #of tasks otherwise its not possible

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

                    