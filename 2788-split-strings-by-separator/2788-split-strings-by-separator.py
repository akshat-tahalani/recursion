#array of strings 
#separator as the character
#each string is split by sperator






class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        ans = []
        word = []
        new = []
        yo = ''

        for i in words:
            new = i.split(separator)
            filtered = [item for item in new if item != ""]


            word.extend(filtered)
            

        return word
            
        