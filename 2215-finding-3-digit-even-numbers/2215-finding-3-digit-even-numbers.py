class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if(i==j or j==k or i==k):
                        continue
                    
                    n = 100 * digits[i] + 10 * digits[j] + digits[k]

                    if(n>=100 and n%2==0):
                        ans.add(n)
        
        return(sorted(ans))