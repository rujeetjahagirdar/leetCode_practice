class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i=j=0
        count=0

        while(j<len(chars)):
            c = chars[j]
            count=1
            j+=1

            while(j<len(chars) and chars[j]==c):
                count+=1
                j+=1
            
            chars[i]=c
            i+=1

            if(count>1):
                for x in str(count):
                    chars[i]=x
                    i+=1
        return i