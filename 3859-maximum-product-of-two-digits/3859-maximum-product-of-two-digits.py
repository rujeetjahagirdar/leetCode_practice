class Solution:
    def maxProduct(self, n: int) -> int:
        
        freq = defaultdict(int)

        while(n>0):
            freq[n%10]+=1
            n//=10
        
        print(freq)

        keys = sorted(freq.keys())
        if(freq[keys[-1]]>=2):
            return keys[-1]**2
        else:
            return keys[-1]*keys[-2]