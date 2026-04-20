#i learned that our goalin this question is that e have to achieve the greedy approach of finding ou the max 1000 digit and then divide but how can we do thata if i assume e take 1000 ohhhhhhhhh its given in the question that max numb is 10000

# iant to take the max number 10000
# then i want to keep dividing it by 10 till i find 6
#but there is a roble




class Solution:
    def maximum69Number (self, num: int) -> int:
        
        div = 1

        while div *10 <= num:
            div *= 10

        #agar me isko itna dbadha lunga toh

        while div > 0 and num // div % 10 == 9 :
        
            div//= 10
        
        if div > 0 and num //div %10 == 6:
            num = num + div*3
        
       
        return num
        
