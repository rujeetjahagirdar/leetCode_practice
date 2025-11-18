class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i=j=0
        # freq=1
        singles=0
        groups=0
        while(i<len(chars)):

            char = chars[i]
            # j=i+1
            count=0
            while(i<len(chars) and chars[i]==char):
                i+=1
                count+=1
            
            chars[j]=char
            j+=1

            if(count>1):
                for digit in str(count):
                    chars[j]=digit
                    j+=1
            
            
            

            # while(i<len(chars) and chars[i]==chars[j]):
            #     # freq+=1
            #     i+=1
            # if(i>j+1):
            #     groups+=1
                
            #     strFreq = str((i-j))
            #     groups+=len(strFreq)
            #     chars[j+1: j+1+len(strFreq)] = strFreq
            #     j=j+1+len(strFreq)
            # else:
            #     singles+=1
            # j=i
            # i+=1
        print(chars)
        print(singles)
        print(groups)

        return j