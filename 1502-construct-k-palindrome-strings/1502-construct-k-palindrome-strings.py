class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if(k>len(s)):
            return False
        elif(k==len(s)):
            return True
        else:
            c = Counter(s)
            oddFreqCount = 0
            for i in c :
                if(c[i]%2!=0):
                    oddFreqCount+=1
            
            if(oddFreqCount<=k):
                return True
            return False