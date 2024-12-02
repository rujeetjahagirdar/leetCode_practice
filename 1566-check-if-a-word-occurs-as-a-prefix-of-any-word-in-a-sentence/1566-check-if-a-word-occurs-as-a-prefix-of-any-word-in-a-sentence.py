class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def checkPrefix(w1, w2):
            # if(w2.startswith(w1)):
            #     return True
            # return False
            n = len(w1)
            if(n>len(w2)):
                return False

            i=0
            while(i<n):
                if(w1[i]==w2[i]):
                    i+=1
                else:
                    return False
            return True
            
        
        sentenceArray = sentence.split(" ")
        for i in range(len(sentenceArray)):
            if(checkPrefix(searchWord, sentenceArray[i])):
                return i+1
        return -1