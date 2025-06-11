class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        a1_freq = float('-inf')
        a2_freq = float('inf')

        for i in c:
            if(c[i]%2==0 and c[i]<a2_freq):
                a2_freq = c[i]
            if(c[i]%2!=0 and c[i]>a1_freq):
                a1_freq = c[i]
        
        print(a1_freq)
        print(a2_freq)

        return(a1_freq - a2_freq)