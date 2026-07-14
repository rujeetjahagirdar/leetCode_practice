class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        sequence = "123456789"
        ans = []

        for lng in range(len(str(low)), len(str(high))+1):
            for l in range(len(sequence)-lng +1):
                n = int(sequence[l:l+lng])
                print(n)
                if(n>=low and n<=high):
                    ans.append(n)
        
        return(ans)