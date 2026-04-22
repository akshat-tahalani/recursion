#boxes into a truck

#boxtypes array

#boxtypes[i] = numbox , numunits

#trucize max numbox
#return max numunits




class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans  = 0 
        rem = truckSize
        i=0

        while rem > 0 and i < len(boxTypes):
            
            if rem > boxTypes[i][0]:
                ans += boxTypes[i][0] * boxTypes[i][1]
                rem -= boxTypes[i][0]

            else :
                ans += rem * boxTypes[i][1]
                rem  = 0
            i+=1
        return ans



        

        
        