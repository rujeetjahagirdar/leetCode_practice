class Solution:
    def binaryGap(self, n: int) -> int:
        bin_str = bin(n)
        ans=0
        i=0

        while(i<len(bin_str)):
            if(bin_str[i]=='1'):
                j=i+1
                while(j<len(bin_str) and bin_str[j]=='0'):
                    j+=1
                if(j<len(bin_str)):
                    ans=max(ans, (j-i))
                    # print(ans)
                i=j
            else:
                i+=1
        
        return ans